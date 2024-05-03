import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# Leitura do dataset
data = pd.read_csv('heart-2024-1-1bimestre.csv')

# Verificação inicial dos dados
print(data.head())
print(data.info())

# Tratamento de possíveis valores nulos
print(data.isnull().sum())
data = data.dropna()  # Remove linhas com valores nulos

# Codificação de variáveis categóricas usando OneHotEncoder
categorical_cols = ['Sex', 'ChestPainType', 'ExerciseAngina', 'ST_Slope']  # Colunas categóricas nominais
data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

# Normalização de variáveis numéricas
scaler = StandardScaler()
numerical_cols = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']  # Colunas numéricas
data[numerical_cols] = scaler.fit_transform(data[numerical_cols])

# Separando as features e o target
X = data.drop('HeartDisease', axis=1)
y = data['HeartDisease']

# Divisão em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Configuração e Treinamento:

# Árvore de Decisão
dt = DecisionTreeClassifier(max_depth=5)
dt.fit(X_train, y_train)

# SVM
svm = SVC(kernel='linear', C=1.0)
svm.fit(X_train, y_train)

# k-NN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Avaliação para cada modelo
for model in [dt, svm, knn]:
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))
