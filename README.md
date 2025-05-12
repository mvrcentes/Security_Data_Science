# 🧪 Laboratorio 8 & 9 — Clasificación de Malware con Deep Learning + Defensa Adversaria

**Autores**  
🧑‍💻 *Marco Ramírez*  
👩‍💻 *Rebecca Smith*  

---

## 📚 Descripción

Este laboratorio tiene como objetivo construir un modelo de red neuronal convolucional (CNN) para clasificar imágenes de malware utilizando un enfoque de aprendizaje profundo. Posteriormente, se evalúa su vulnerabilidad frente a ataques adversarios y se implementa una defensa robusta usando entrenamiento adversario.

---

## 📁 Estructura del proyecto

- `malimg_paper_dataset_imgs/` — Directorio con imágenes de malware clasificadas por familia.
- `modelo_malware.h5` — Modelo CNN entrenado y guardado.
- `La8.py` — Código del laboratorio (exploración, entrenamiento, ataques y defensa).

---

## 🔍 Parte 1: Clasificación de Malware

### 📊 Exploración del dataset

- Se identificaron las familias con más de **100 imágenes**.
- Se excluyeron clases poco representadas para evitar sobreajuste.
- Se generaron gráficos de barras con la distribución por familia.

### 🖼️ Visualización

- Se muestra un collage de imágenes aleatorias de distintas familias para tener una idea visual de los datos.

### 🧠 Construcción y entrenamiento del modelo

- Arquitectura de red neuronal convolucional:
  - `Conv2D(32)` + `MaxPooling`
  - `Conv2D(64)` + `MaxPooling`
  - `Flatten + Dense(128)` + `Dropout`
  - `Softmax` final para clasificación multiclase

- Entrenamiento:
  - `epochs=15`
  - `batch_size=32`

- Métricas visualizadas:
  - Precisión y pérdida por época (entrenamiento vs validación)

### 📈 Evaluación

- Reporte de clasificación (`sklearn`)
- Matriz de confusión (`seaborn`)
- Métricas:
  - *Accuracy final en test set*

---

## 💣 Parte 2: Ataques Adversarios

Se utiliza el framework [ART (Adversarial Robustness Toolbox)](https://github.com/Trusted-AI/adversarial-robustness-toolbox) para evaluar la vulnerabilidad del modelo.

### 🔺 Fast Gradient Method (FGM)

- `eps = 0.2`
- Precisión bajo ataque: **4.84%**

### 🔻 Projected Gradient Descent (PGD)

- `eps = 0.2`, `iteraciones = 40`
- Precisión bajo ataque: **0.40%**

Estos resultados muestran la **alta sensibilidad del modelo** ante ejemplos adversarios.

---

## 🛡️ Defensa: Adversarial Training (Madry PGD)

Se implementa entrenamiento adversario usando el mismo tipo de ataque (PGD) como parte del proceso de entrenamiento del modelo.

- `epochs = 10`
- Se entrena con ejemplos reales y adversarios generados en tiempo real

---

## ✅ Resultados Comparativos

| Condición           | Precisión antes | Precisión después |
|---------------------|------------------|--------------------|
| Datos limpios       | —                | **71.15%**         |
| FGM (ε = 0.2)        | **4.84%**         | **69.48%**         |
| PGD (ε = 0.2)        | **0.40%**         | **69.88%**         |

> 🔐 *La defensa mejoró drásticamente la robustez del modelo ante ataques.*

---

## 📌 Conclusiones

- Las CNN pueden clasificar imágenes de malware con alta precisión.
- Sin embargo, son extremadamente vulnerables a pequeñas perturbaciones adversarias.
- El entrenamiento adversario mejora la resistencia del modelo de manera significativa sin alterar su arquitectura original.

---

## 🧠 Requisitos

- Python ≥ 3.8
- TensorFlow
- ART (Adversarial Robustness Toolbox)
- Scikit-learn
- Matplotlib, Seaborn
- Pandas, NumPy

---

## 🚀 Ejecutar

```bash
pip install -r requirements.txt
python La8.py