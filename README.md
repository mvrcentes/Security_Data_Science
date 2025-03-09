# Security_Data_Science
# Laboratorio #4 - Familias de Malware

Este notebook está diseñado para explorar y analizar familias de malware. En el laboratorio, se desarrollan técnicas para identificar y clasificar archivos de malware basándose en sus características.

## Descripción del Proyecto

En este proyecto, se recopilan y procesan archivos de malware para su análisis. El objetivo es estudiar cómo se pueden identificar y diferenciar diversas familias de malware a partir de los metadatos y características de los archivos.

## Requisitos

- Python 3.x
- Librerías necesarias:
    - `pefile` (para analizar archivos PE)
    - `pandas` (para el manejo de datos)
    - `hashlib` (para la generación de hash)
    - `re` (para la manipulación de expresiones regulares)
    - `datetime` (para trabajar con fechas y horas)
    - `subprocess` (para ejecutar comandos en el sistema)

## Estructura del Notebook

1. Parte 1: Importación de librerías
Se importan las librerías necesarias para el análisis de malware.

2. Creación del Dataset
Se crean listas de archivos de malware para su posterior análisis.

3. Análisis de Archivos de Malware
Se exploran los archivos PE y se extraen características relevantes como hashes, tamaño de archivo y más.
