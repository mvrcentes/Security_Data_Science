import os
import networkx
from networkx.drawing.nx_pydot import write_dot
import itertools
import subprocess
import pydot
from IPython.display import Image

# Función Jaccard para calcular la similitud
def jaccard(set1, set2):
    intersection = set1.intersection(set2)
    intersection_length = float(len(intersection))
    union = set1.union(set2)
    union_length = float(len(union))
    return intersection_length / union_length

# Función para extraer las cadenas del archivo binario
def getstrings(fullpath):
    result = subprocess.run(["strings", fullpath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        strings = result.stdout.decode().split("\n")
        return set(strings)
    return set()

# Función para obtener las "llamadas a funciones" (esto es solo un ejemplo, puedes ajustarlo según tu análisis)
def getfunctions(fullpath):
    result = subprocess.run(["nm", fullpath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        functions = result.stdout.decode().split("\n")
        return set(functions)
    return set()

# Verificar si el archivo es un ejecutable PE
def pecheck(fullpath):
    with open(fullpath, "rb") as f:
        return f.read(2) == b"MZ"

# Crear un grafo por familia
def create_family_graph(malware_paths, malware_attributes, threshold, feature_type):
    graph = networkx.Graph()
    for malware1, malware2 in itertools.combinations(malware_paths, 2):
        # Seleccionamos la característica (strings o funciones)
        if feature_type == "strings":
            set1 = malware_attributes[malware1]["strings"]
            set2 = malware_attributes[malware2]["strings"]
        elif feature_type == "functions":
            set1 = malware_attributes[malware1]["functions"]
            set2 = malware_attributes[malware2]["functions"]
        else:
            raise ValueError("Feature type must be 'strings' or 'functions'.")

        jaccard_index = jaccard(set1, set2)

        if jaccard_index > threshold:
            graph.add_edge(malware1, malware2, penwidth=1 + (jaccard_index - threshold) * 10)

    return graph

# Análisis general
def analyze_malware(target_directory, thresholds, output_dot_file):
    malware_paths = []
    malware_attributes = dict()
    family_graphs = dict()  # Diccionario para los grafos de cada familia
    all_malware_graph = networkx.Graph()  # Grafo global de todos los malware

    # Recorremos el directorio para obtener los archivos de malware
    for root, dirs, paths in os.walk(target_directory):
        for path in paths:
            full_path = os.path.join(root, path)
            malware_paths.append(full_path)

    # Filtramos los archivos que no sean PE
    malware_paths = [path for path in malware_paths if pecheck(path)]

    # Extraemos las características (strings y funciones) de todos los archivos de malware
    for path in malware_paths:
        strings = getstrings(path)
        functions = getfunctions(path)
        malware_attributes[path] = {"strings": strings, "functions": functions}

        # Añadimos cada archivo de malware al grafo global
        all_malware_graph.add_node(path, label=os.path.split(path)[-1][:10])

    # Realizamos el análisis con diferentes umbrales y características
    for threshold in thresholds:
        for feature_type in ["strings", "functions"]:
            # Grafo general
            graph = create_family_graph(malware_paths, malware_attributes, threshold, feature_type)
            write_dot(graph, f"{output_dot_file}_threshold_{threshold}_{feature_type}.dot")
            print(f"Graph for threshold {threshold} and feature {feature_type} written to {output_dot_file}_threshold_{threshold}_{feature_type}.dot")

            # Grafo por familia (esto asume que los directorios son las familias)
            for family in set([os.path.dirname(path) for path in malware_paths]):
                family_malware_paths = [path for path in malware_paths if os.path.dirname(path) == family]
                family_graph = create_family_graph(family_malware_paths, malware_attributes, threshold, feature_type)
                write_dot(family_graph, f"{output_dot_file}_family_{family.replace('/', '_')}_threshold_{threshold}_{feature_type}.dot")
                print(f"Family graph for {family} and threshold {threshold} and feature {feature_type} written to {output_dot_file}_family_{family.replace('/', '_')}_threshold_{threshold}_{feature_type}.dot")

    # Grafo general de todos los malware
    write_dot(all_malware_graph, f"{output_dot_file}_all_malware.dot")
    print(f"All malware graph written to {output_dot_file}_all_malware.dot")

    # Llamamos a la función para dibujar todos los grafos
    draw_all_graphs(output_dot_file)

# Función para dibujar todos los grafos generados y guardarlos como imágenes
def draw_all_graphs(output_dot_file):
    dot_files = [f for f in os.listdir() if f.endswith('.dot') and f.startswith(output_dot_file)]
    for dot_file in dot_files:
        # Cargar el archivo DOT
        graph = pydot.graph_from_dot_file(dot_file)[0]
        # Convertir a imagen PNG
        output_image = dot_file.replace('.dot', '.png')
        graph.write_png(output_image)
        print(f"Graph {dot_file} has been converted to {output_image}")
        
        # Mostrar la imagen (opcional si estás en Jupyter Notebook)
        Image(filename=output_image)

# Parámetros de entrada
target_directory = "MALWR"  # Cambia la ruta a tu directorio
output_dot_file = "salida.dot"
thresholds = [0.6, 0.8, 0.9]  # Tres umbrales distintos

# Ejecutar el análisis
analyze_malware(target_directory, thresholds, output_dot_file)