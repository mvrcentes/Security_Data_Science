# **Security_Data_Science**  
# 📌 **Laboratorio #3 – Detección de Malware mediante Secuencias de Llamadas a API**  

## 📖 **Objetivos**  
- Implementar modelos de **Machine Learning (ML)** y **Deep Learning (DL)** para la detección de malware basados en el análisis dinámico de llamadas a API.  
- Evaluar y comparar ambos enfoques para determinar cuál ofrece mejores resultados en términos de precisión y capacidad de detección.  

## 📂 **Contenido del Proyecto**  
El laboratorio está desarrollado en un **Jupyter Notebook (`.ipynb`)** e incluye los siguientes pasos:  

### **1. Carga y preprocesamiento de datos**  
   - Lectura del dataset con las secuencias de llamadas a API.  
   - Limpieza y transformación de los datos.  
   - División en conjuntos de entrenamiento y prueba.  

### **2. Implementación de Modelos**  
   - **Modelo 1 (Machine Learning con Naive Bayes)**  
     - Representación de las llamadas a API mediante **TF-IDF**.  
     - Entrenamiento con **Naive Bayes Multinomial**.  
     - Evaluación con validación cruzada (k=10).  

   - **Modelo 2 (Deep Learning con Redes Neuronales)**  
     - Generación de **embeddings** a partir de modelos NLP (`SentenceTransformers`).  
     - Implementación de una **Red Neuronal Artificial (ANN)** con capas densas y dropout.  
     - Entrenamiento y ajuste del modelo con optimizador **Adam**.  

### **3. Evaluación de Modelos**  
   - Cálculo de métricas clave para cada modelo:  
     - **Precisión (Accuracy)**  
     - **Precisión y Recall (Precision & Recall)**  
     - **Curva ROC-AUC**  
   - Comparación de resultados y análisis de rendimiento.  

### **4. Comparación y Análisis de Impacto**  
   - Evaluación de la capacidad de cada modelo para detectar malware.  
   - Discusión sobre la importancia de capturar patrones en las llamadas a API.  
   - Análisis de falsos positivos y falsos negativos.  

## 📊 **Modelos Utilizados**  

- **Modelo 1: Naive Bayes con TF-IDF**  
  - Utiliza **frecuencia de términos (TF-IDF)** para representar las llamadas a API.  
  - Se basa en **Naive Bayes Multinomial**, un algoritmo probabilístico eficiente para clasificación de texto.  
  - **Precisión obtenida: 82.44%**.  
  - **Área bajo la curva ROC (AUC): 0.95**.  

- **Modelo 2: Redes Neuronales con Embeddings**  
  - Emplea **embeddings generados con NLP (SentenceTransformers)** para capturar mejor las relaciones semánticas entre las llamadas a API.  
  - Se entrena una **Red Neuronal Artificial (ANN)** con múltiples capas densas y dropout.  
  - **Precisión obtenida: 94.72%**.  
  - **Área bajo la curva ROC (AUC): 0.97**.  

## 📌 **Requisitos**  
Para ejecutar el laboratorio, asegúrate de tener instaladas las siguientes bibliotecas de Python:  

```python
pip install -r requirements.txt
```

# 🚀 Cómo ejecutar el laboratorio
	1.	Descarga el archivo Lab3.ipynb.
	2.	Asegúrate de tener instaladas las bibliotecas necesarias.
	3.	Abre el Jupyter Notebook y ejecuta las celdas secuencialmente.
	4.	Analiza los resultados y compara los modelos.

# 🏆 Resultados y Conclusiones

Después de comparar los modelos:
	•	El Modelo 2 (Redes Neuronales) superó al Modelo 1 en todas las métricas, con una precisión del 94.72% frente al 82.44% del Modelo 1.
	•	El Modelo 2 también logró una mejor capacidad de discriminación entre malware y benignos (AUC=0.97 vs. AUC=0.95).
	•	Sin embargo, el Modelo 1 es más rápido y computacionalmente eficiente, lo que puede ser útil en escenarios donde los recursos son limitados.

El análisis mostró que el uso de embeddings y redes neuronales permite mejorar significativamente la detección de malware, alineándose con lo descrito en el artículo “Automated Behaviour-Based Malware Detection 
Framework Based on NLP and Deep Learning Techniques”. No obstante, si se requiere una solución más ligera y rápida, el Modelo 1 sigue siendo una alternativa viable.

---

✉️ **Autores:** *Marco Ramírez y Rebecca Smith*  
📅 **Última actualización:** *02-03-2025*  

---
