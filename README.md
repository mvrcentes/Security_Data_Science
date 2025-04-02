# 🧪 Laboratorio #6 – Análisis de tráfico de red
**Curso:** Security Data Science   

---

## 📁 Archivo analizado

- `analisis_paquetes.pcap`
- Se utilizó la librería `scapy` para leer los paquetes y `pandas` para convertirlos en un DataFrame.

---

## 📊 Análisis estadístico

### ✅ IPs únicas

- IPs origen únicas:  
  Se identificaron varias, pero la más frecuente fue `10.1.10.53`.

- IPs destino más frecuentes:  
  La IP `84.54.22.33` recibió la mayor cantidad de tráfico.

---

### ✅ Puertos

- **Puerto destino más común:** `53`  
  - Este puerto está asociado al servicio **DNS**.
  - Su propósito es la **resolución de nombres de dominio**.
  
- **Puertos origen utilizados:**
  - `15812`, `23903` (puertos efímeros)
  - También `53`, lo cual **no es común** para un cliente. Esto sugiere que `10.1.10.53` podría estar actuando como servidor DNS o participando en una actividad sospechosa.

---

### 📈 Visualización del tráfico

- Se generaron gráficas de barras para visualizar:
  - Bytes enviados por IP origen.
  - Bytes recibidos por IP destino.
  - Bytes agrupados por puertos de origen y destino.
  - Evolución del tráfico por segundo para la IP `10.1.10.53`.

---

## 🕵️‍♀️ Investigación de la IP más frecuente

### 🔹 Paso 1: IP origen más activa
- `10.1.10.53`

### 🔹 Paso 2: IP destino con mayor intercambio
- `84.54.22.33`

### 🔹 Paso 3: Conversación entre ambas IPs
- Se creó un nuevo DataFrame `df_conversacion` que contiene **todo el tráfico bidireccional entre estas dos IPs**.

---

## 📦 Análisis de Payloads

### 🔹 Extracción

- Se extrajeron todos los payloads (`Raw.load`) que forman parte de la conversación entre `10.1.10.53` y `84.54.22.33`.
- Los payloads fueron almacenados en un array `payloads_array`.

### 🔹 Contenido binario (primeros bytes en hex)

Se observó el siguiente patrón (ejemplo):
Payload 0 (primeros 64 bytes en hex):
ef bf bd 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00 01 62 00 00 00 ef bf bd 08 06 00 00

Aunque comienza con bytes ilegibles (`ef bf bd`), luego se observa claramente el header de un archivo **PNG**: `50 4E 47 0D 0A 1A 0A`.

### 🔹 Contenido ASCII estimado

```text
Payload 0 (ASCII estimado):
...PNG........IHDR...b...........(...TR..:...IDATx...
```
Esto confirma la presencia de una imagen PNG dentro del payload, enviada a través del puerto DNS (53), lo cual no es normal.
