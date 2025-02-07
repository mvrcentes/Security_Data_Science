# Security_Data_Science
# 📌 Laboratorio #1 – Detección de Pishing

## 📖 Objetivos
- Realizar una revisión de literatura para identificar características potenciales en las URLs de
Phishing
- Implementar un modelo de ML para clasificar si un dominio es legítimo o es Phishing

## 📂 Contenido del Proyecto  
El laboratorio está desarrollado en un **Jupyter Notebook (`.ipynb`)** e incluye los siguientes pasos:

1. **Carga y preprocesamiento de datos**  
   - Lectura del dataset  
   - Limpieza y transformación de datos  
   - División en conjuntos de entrenamiento y prueba  

2. **Entrenamiento de modelos**  
   - Implementación de **SVM**  
   - Implementación de **Random Forest**  

3. **Evaluación de modelos**  
   - Cálculo de métricas clave:  
     - Precisión (*Accuracy*)  
     - Precisión y Recall (*Precision & Recall*)  
     - F1-score  
     - Curva ROC-AUC  
   - Comparación de resultados  

4. **Análisis de impacto**  
   - Discusión sobre el impacto de falsos positivos y falsos negativos  
   - Elección del mejor modelo basado en métricas  

## 📊 Modelos utilizados  
- **SVM (Support Vector Machine)**: Modelo basado en hiperplanos para la clasificación de datos. Se probó con diferentes kernels para evaluar su rendimiento.  
- **Random Forest**: Algoritmo de ensamblado basado en múltiples árboles de decisión, utilizado para mejorar la precisión y reducir el sobreajuste.  

## 📌 Requisitos  
Para ejecutar el laboratorio, asegúrate de tener instaladas las siguientes bibliotecas de Python:

```python
pip install -r requirements.txt
```

## 🚀 Cómo ejecutar el laboratorio  
1. Descarga el archivo `phishing_classification.ipynb`.  
2. Asegúrate de tener instaladas las bibliotecas necesarias.  
3. Abre el **Jupyter Notebook** y ejecuta las celdas secuencialmente.  
4. Analiza los resultados y compara los modelos.  

## 🏆 Resultados y Conclusiones  
Después de comparar los modelos:  
- **SVM obtuvo una precisión del 82%**, mostrando un buen equilibrio entre precisión y recall.  
- **Random Forest obtuvo entre 79%-81% de precisión**, con una buena capacidad de generalización.  

El SVM fue seleccionado como el mejor modelo en este caso debido a su mayor rendimiento. Sin embargo, el análisis de falsos positivos y falsos negativos mostró la importancia de ajustar los parámetros para mejorar su efectividad.

---

✉️ **Autores:** *Marco Ramírez y Rebecca Smith*  
📅 **Última actualización:** *6-02-2025*  

---
