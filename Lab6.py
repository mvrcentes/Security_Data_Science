#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/python .venv


# # Laboratorio #6 - Análisis de tráfico de red
# 

# ## Análisis estadístico
# 

# ### Cargar el archvio
# 

# In[1]:


from scapy.all import rdpcap

# Asignar el archivo .pcap a una variable
pcap_file = "analisis_paquetes.pcap"
packets = rdpcap(pcap_file)

# Verifica el tipo y cantidad de paquetes
print(type(packets))
print(len(packets))
print(packets.summary())


# ### Convertirlo a un Dataframe
# 

# In[3]:


import pandas as pd

# Lista para almacenar la info de cada paquete
packet_data = []

for pkt in packets:
    if pkt.haslayer("IP"):  # Solo si tiene capa IP
        src = pkt["IP"].src
        dst = pkt["IP"].dst
        sport = pkt.sport if hasattr(pkt, "sport") else None
        dport = pkt.dport if hasattr(pkt, "dport") else None
        payload_len = len(pkt.payload)

        packet_data.append(
            {
                "src": src,
                "dst": dst,
                "sport": sport,
                "dport": dport,
                "payload_len": payload_len,
                "time": pkt.time,
            }
        )

# Convertir a DataFrame
df = pd.DataFrame(packet_data)

# Mostrar las primeras filas
df.head(5)


# ### Estadísticas

# #### Mostrar todas las IP origen única

# In[4]:


ip_origenes = df["src"].unique()
print("IPs origen únicas:")
print(ip_origenes)


# In[5]:


# Contar ocurrencias de cada IP origen
conteo_ip_origen = df["src"].value_counts()
print("Conteo de IPs origen:")
print(conteo_ip_origen)


# #### Mostrar todas las IP destino

# In[6]:


# Mostrar todas las IP destino únicas
ip_destinos = df["dst"].unique()
print("IPs destino únicas:")
print(ip_destinos)


# In[7]:


# Contar ocurrencias de cada IP destino
conteo_ip_destino = df["dst"].value_counts()
print("Conteo de IPs destino:")
print(conteo_ip_destino)


# #### ¿Cuál es la IP de origen más frecuente?
# 
# IP origen `10.1.10.53`

# ##### ¿A qué IP destino se comunica con más frecuencia?

# In[8]:


# Filtrar solo paquetes donde la IP origen es 10.1.10.53
df_origen_10 = df[df["src"] == "10.1.10.53"]

# Contar las IP destino a las que se comunica esa IP origen
destinos_mas_frecuentes = df_origen_10["dst"].value_counts()

print("Destinos más frecuentes para 10.1.10.53:")
print(destinos_mas_frecuentes)


# IP de destino más frecuente `84.54.22.33`

# ##### ¿A que puerto destino se comunica? ¿Cuál es el propósito de este puerto?

# In[9]:


# Contar los puertos destino a los que se comunica 10.1.10.53
puertos_destino_frecuentes = df_origen_10["dport"].value_counts()

print("Puertos destino más frecuentes para 10.1.10.53:")
print(puertos_destino_frecuentes)


# * **Puerto de destino**: `53` (DNS)
# * **Propostio**: DNS (Domain Name System) es un sistema que traduce nombres de dominio legibles por humanos (como www.ejemplo.com) en direcciones IP numéricas (como 192.168.1.1), que son necesarias para localizar y acceder a dispositivos en la red de Internet.
# 
# Referencia: https://books.spartan-cybersec.com/cppj/networking-for-juniors/puertos-y-servicios/puerto-53-dns

# ##### ¿Desde que puertos origen se comunica?

# In[10]:


# Contar los puertos origen desde los que se comunica 10.1.10.53
puertos_origen_frecuentes = df_origen_10["sport"].value_counts()

print("Puertos origen más frecuentes para 10.1.10.53:")
print(puertos_origen_frecuentes)


# * **Puertos de origen**:
#     * 53
#     * 15812
#     * 23903

# ### Gráficas

# #### a. Genere una gráfica de barras 2D horizontales, en el eje Y las IPs origen, y en el eje X lasuma de los payloads (bytes) enviados desde dichas direcciones.

# In[11]:


import matplotlib.pyplot as plt

# Agrupar por IP origen y sumar los payloads
payloads_por_ip_origen = df.groupby("src")["payload_len"].sum().sort_values(ascending=True)

# Crear la gráfica
plt.figure(figsize=(10, 6))
payloads_por_ip_origen.plot(kind="barh")
plt.xlabel("Suma de Payloads (bytes)")
plt.ylabel("IP Origen")
plt.title("Bytes enviados por IP Origen")
plt.tight_layout()
plt.show()


# #### b. Genere una gráfica de barras 2D horizontales, en el eje Y las IP destino, y en el eje X la suma de los payloads (bytes) recibidos en dichas direcciones.

# In[12]:


# Agrupar por IP destino y sumar los payloads recibidos
payloads_por_ip_destino = df.groupby("dst")["payload_len"].sum().sort_values(ascending=True)

# Crear la gráfica
plt.figure(figsize=(10, 6))
payloads_por_ip_destino.plot(kind="barh")
plt.xlabel("Suma de Payloads (bytes)")
plt.ylabel("IP Destino")
plt.title("Bytes recibidos por IP Destino")
plt.tight_layout()
plt.show()


# #### c. Genere una gráfica de barras 2D horizontales, en el eje Y los puertos origen, y en el eje X la suma de los payloads (bytes) enviados de dichos puertos.

# In[13]:


# Agrupar por puerto de origen y sumar los payloads enviados
payloads_por_puerto_origen = df.groupby("sport")["payload_len"].sum().sort_values(ascending=True)

# Crear la gráfica
plt.figure(figsize=(10, 6))
payloads_por_puerto_origen.plot(kind="barh")
plt.xlabel("Suma de Payloads (bytes)")
plt.ylabel("Puerto Origen")
plt.title("Bytes enviados por Puerto de Origen")
plt.tight_layout()
plt.show()


# #### d. Genere una gráfica 2D de barras horizontales, en el eje Y los puertos destino, y en el eje X la suma de los payloads (bytes) recibidos en dichos puertos.

# In[14]:


# Agrupar por puerto de destino y sumar los payloads recibidos
payloads_por_puerto_destino = df.groupby("dport")["payload_len"].sum().sort_values(ascending=True)

# Crear la gráfica
plt.figure(figsize=(10, 6))
payloads_por_puerto_destino.plot(kind="barh")
plt.xlabel("Suma de Payloads (bytes)")
plt.ylabel("Puerto Destino")
plt.title("Bytes recibidos por Puerto de Destino")
plt.tight_layout()
plt.show()


# #### e. Genere una gráfica de barras 2D verticales, en el eje Y la suma de los payload, en el eje X el tiempo, para la IP origen más frecuente.

# In[16]:


# Filtrar solo paquetes de la IP origen más frecuente
df_10 = df[df["src"] == "10.1.10.53"].copy()

# Redondear el tiempo a segundos (opcional: puedes agrupar por segundos o minutos según convenga)
df_10["time_rounded"] = pd.to_datetime(df_10["time"].astype(float), unit='s').dt.floor("S")

# Agrupar por tiempo y sumar payloads
payloads_por_tiempo = df_10.groupby("time_rounded")["payload_len"].sum()

# Crear la gráfica
plt.figure(figsize=(12, 6))
payloads_por_tiempo.plot(kind="bar")
plt.ylabel("Suma de Payloads (bytes)")
plt.xlabel("Tiempo")
plt.title("Payload enviado por 10.1.10.53 a lo largo del tiempo")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# #### f. Utilizando la información de las estadísticas y la información del comportamiento del tráfico que las gráficas muestran, describa que es lo que está sucediendo. ¿Es común el comportamiento?
# 
# 1. IP origen más activa: 10.1.10.53
# 	* Es la IP que más paquetes ha enviado.
# 	* Se comunica principalmente con la IP 84.54.22.33.
# 
# 2. IP destino más frecuente: 84.54.22.33
# 	* Recibe la mayor cantidad de datos desde 10.1.10.53.
# 
# 3. Puerto destino más común: 53
# 	* Este puerto está asociado al servicio DNS (Domain Name System).
# 	* Indica que el tráfico está relacionado con consultas de resolución de nombres.
# 
# 4. Puertos origen:
# 	* Se observan puertos efímeros (por ejemplo, 23903, 15812), lo cual es típico del cliente al iniciar conexiones.
# 	* También hay tráfico desde el puerto 53, lo que podría indicar que 10.1.10.53 también está actuando como servidor DNS, lo cual no es común si esta IP pertenece a un cliente típico.
# 
# 5. Payloads a lo largo del tiempo
# 	* El volumen de datos enviados por segundo se mantiene relativamente constante, con ligeras variaciones.
# 	* No hay picos bruscos, lo que sugiere un comportamiento automatizado o regular.
# 
# Es normal sí, si:
# * 10.1.10.53 es un servidor DNS interno dentro de una red corporativa o universitaria.
# * En ese caso, es normal que se comunique constantemente con clientes o servidores externos para resolver nombres de dominio.
# 
# No, si: 
# * No es típico que un cliente se comunique tanto con el puerto 53 de forma tan constante.
# * Tampoco es común que un cliente use el puerto 53 como origen, lo que sugiere que puede estar respondiendo consultas → esto implicaría un comportamiento sospechoso como:
# * Actuar como DNS sin autorización.
# * Ser parte de una botnet o malware que utiliza DNS para comunicación encubierta.
# 
# pero una ip 10.1... comunmente se usa como una ip privada (interna)
# 
# 1. Servidor DNS interno legítimo → tráfico normal.
# 2. Cliente que actúa como servidor DNS (intencional o no) → comportamiento sospechoso o malicioso.
# 3. DNS tunneling: técnica usada por malware para evadir firewalls y extraer datos a través de tráfico DNS.
# 

# ### Investigación del payload

# #### a. Cree un nuevo DF que incluya únicamente las conexiones con la dirección IP origen más frecuente.

# In[17]:


# Crear un nuevo DataFrame con conexiones desde la IP origen más frecuente
ip_mas_frecuente = df["src"].value_counts().idxmax()  # Esto obtiene automáticamente la IP más frecuente
df_ip_frecuente = df[df["src"] == ip_mas_frecuente].copy()

# Ver las primeras filas para verificar
df_ip_frecuente.head()


# #### b. Cree un nuevo DF que utilice el DF anterior con las columnas src, dst y payload y agrúpelas por dst y la suma del payload

# In[18]:


# Seleccionar columnas necesarias
df_dst_payload = df_ip_frecuente[["src", "dst", "payload_len"]]

# Agrupar por destino y sumar los payloads
df_payload_por_destino = df_dst_payload.groupby("dst")["payload_len"].sum().reset_index()

# Mostrar el resultado
df_payload_por_destino


# #### c. Obtenga la IP destino que más ha intercambiado bytes con la IP más frecuente. Esta IP es sospechosa por la cantidad de bytes intercambiados, entre todas las direcciones.

# In[19]:


# Obtener la IP destino con mayor cantidad de bytes intercambiados
ip_destino_top = df_payload_por_destino.loc[df_payload_por_destino["payload_len"].idxmax()]

print("La IP destino que más ha intercambiado bytes con la IP origen más frecuente es:")
print(ip_destino_top)


# #### d. Cree un nuevo DF con la conversación entre la IP más frecuente y la IP sospechosa.

# In[20]:


# Extraer IPs de interés
ip_origen_frecuente = ip_mas_frecuente
ip_destino_sospechosa = ip_destino_top["dst"]

# Filtrar todas las filas donde haya comunicación entre estas dos IPs (en cualquier dirección)
df_conversacion = df[
    ((df["src"] == ip_origen_frecuente) & (df["dst"] == ip_destino_sospechosa)) |
    ((df["src"] == ip_destino_sospechosa) & (df["dst"] == ip_origen_frecuente))
].copy()

# Mostrar las primeras filas
df_conversacion.head()


# #### e. Obtenga los payloads del DF del inciso anterior, y añada cada uno en un array.

# In[21]:


from scapy.all import Raw

# Crear un array para guardar los payloads
payloads_array = []

# Iterar sobre los paquetes originales y buscar aquellos que coincidan con la conversación
for pkt in packets:
    if pkt.haslayer("IP"):
        src = pkt["IP"].src
        dst = pkt["IP"].dst

        if (
            (src == ip_origen_frecuente and dst == ip_destino_sospechosa) or
            (src == ip_destino_sospechosa and dst == ip_origen_frecuente)
        ):
            # Verificar si tiene capa Raw (donde usualmente está el payload)
            if pkt.haslayer(Raw):
                payloads_array.append(bytes(pkt[Raw].load))  # Guardar el contenido binario


# #### f. Muestre el contenido del array.

# In[ ]:


for i, p in enumerate(payloads_array[:5]):
    try:
        print(f"Payload {i} (primeros 64 bytes en hex): {p[:64].hex(' ')}\n")
    except UnicodeDecodeError:
        print(f"Payload {i}: Unable to decode payload\n")


# In[33]:


def buscar_firma_en_payload(payload):
    firmas = {
        b"\x89PNG\r\n\x1a\n": "PNG",
        b"\xFF\xD8\xFF": "JPEG",
        b"%PDF": "PDF",
        b"PK\x03\x04": "ZIP / DOCX / XLSX",
    }

    for firma, tipo in firmas.items():
        if firma in payload:
            return tipo

    return "Desconocido"

# Buscar tipos en los payloads
for i, p in enumerate(payloads_array[:5]):
    ascii_legible = ''.join([chr(b) if 32 <= b <= 126 else '.' for b in p[:64]])
    print(f"Payload {i} (ASCII estimado):\n{ascii_legible}\n")

