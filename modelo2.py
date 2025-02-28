import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_curve, auc, classification_report
from sentence_transformers import SentenceTransformer


# Cargar los datos
data = pd.read_csv('Data.csv')
print(data.head())

# Exploración de datos
data['labels'].value_counts().plot(kind='bar')
plt.title("Distribución de Clases (Benigno vs Malware)")
plt.xlabel("Clase")
plt.ylabel("Frecuencia")
plt.show()

# Preprocesamiento: convertir llamadas a API en texto separado por espacio
data['api_calls'] = data.iloc[:, 2:].astype(str).apply(lambda x: ' '.join(x.dropna()), axis=1)
X = data['api_calls']
y = data['labels']

# Generación de embeddings usando un modelo de NLP de Gemini (simulado con Sentence-Transformers)
model_nlp = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # Reemplazar con embeddings de Gemini si están disponibles
X_embeddings = model_nlp.encode(X.tolist(), convert_to_numpy=True)

# División de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_embeddings, y, test_size=0.3, random_state=42, stratify=y)

# Definición de la Red Neuronal
model_nn = Sequential([
    Input(shape=(X_train.shape[1],)),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(1, activation='sigmoid')
])

model_nn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenamiento del modelo
history = model_nn.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, batch_size=32, verbose=1)

# Evaluación del modelo
y_pred_prob = model_nn.predict(X_test).flatten()
y_pred = (y_pred_prob > 0.5).astype(int)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.4f}')
print(f'Precision: {precision:.4f}')
print(f'Recall: {recall:.4f}')
print(classification_report(y_test, y_pred))

# Curva ROC
fpr, tpr, _ = roc_curve(y_test, y_pred_prob)
roc_auc = auc(fpr, tpr)
plt.figure()
plt.plot(fpr, tpr, label=f'Área bajo la curva (AUC) = {roc_auc:.2f}')
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.title('Curva ROC')
plt.legend()
plt.show()
