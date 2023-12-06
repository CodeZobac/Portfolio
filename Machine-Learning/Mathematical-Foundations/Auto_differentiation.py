import numpy as np
x_treino = np.array([1, 2, 3, 4, 5])
y_treino = np.array([5, 7, 9, 11, 13])
m = 0.5
b = 1
aprendizagem = 0.01
rondas = 1000


def calcular_c(y, y2):
    return np.mean((y-y2)**2)


for ronda in range(rondas):
    y2 = m * x_treino + b
    cost = calcular_c(y_treino, y2)

    dm = (-2 / len(x_treino)) * np.sum(x_treino * (y_treino - y2))
    db = (-2 / len(x_treino)) * np.sum(y_treino - y2)

    m = m - aprendizagem * dm
    b = b - aprendizagem * db
    if ronda % 100 == 0:
        print("Ronda {}: Cost = {:.4f}".format(ronda, cost))
        print(m, b)
