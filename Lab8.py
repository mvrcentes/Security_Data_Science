#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/bin/python


# # Laboratorio 8: Clasificación de Malware con DL
# 

# ## 📊 Exploración del dataset
# 

# In[2]:


import os

import pandas as pd

base_path = "malimg_paper_dataset_imgs"
familias = [
    folder
    for folder in os.listdir(base_path)
    if os.path.isdir(os.path.join(base_path, folder))
]
conteo = {
    familia: len(os.listdir(os.path.join(base_path, familia))) for familia in familias
}


pd.Series(conteo).sort_values(ascending=False).plot(
    kind="bar", title="Cantidad de muestras por familia"
)


# ### 🧹 Filtrado de familias con pocas observaciones

# In[3]:


# 📌 Umbral mínimo de imágenes por familia
umbral_minimo = 100

# Filtramos las familias que cumplen con el mínimo
familias_filtradas = [familia for familia, cantidad in conteo.items() if cantidad >= umbral_minimo]

print(f"Se conservarán {len(familias_filtradas)} familias:")
print(familias_filtradas)


# Para mejorar el balance del dataset y evitar el sobreajuste, se excluyen las familias con menos de 100 imágenes.

# ## 🖼️ Visualización de imágenes

# In[4]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

fig, axs = plt.subplots(2, 5, figsize=(15, 6))
for ax in axs.flatten():
    familia = random.choice(familias_filtradas)  # ← aquí el cambio importante
    img_path = os.path.join(
        base_path, familia, random.choice(os.listdir(os.path.join(base_path, familia)))
    )
    img = mpimg.imread(img_path)
    ax.imshow(img, cmap="gray")
    ax.set_title(familia)
    ax.axis("off")
plt.tight_layout()


# ## 📦 Cargar imágenes (64x64, normalizadas):

# In[5]:


import numpy as np
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Dimensiones para redimensionar las imágenes
IMG_SIZE = (64, 64)

X = []
y = []
label_map = {familia: idx for idx, familia in enumerate(familias_filtradas)}

for familia in familias_filtradas:
    carpeta = os.path.join(base_path, familia)
    for archivo in os.listdir(carpeta):
        ruta = os.path.join(carpeta, archivo)
        try:
            # Cargar imagen en escala de grises, redimensionar
            imagen = load_img(ruta, color_mode='grayscale', target_size=IMG_SIZE)
            imagen_array = img_to_array(imagen) / 255.0  # Normalizar
            X.append(imagen_array)
            y.append(label_map[familia])
        except Exception as e:
            print(f"Error al procesar {ruta}: {e}")

X = np.array(X)
y = np.array(y)

print(f"Shape de X: {X.shape}")
print(f"Shape de y: {y.shape}")

