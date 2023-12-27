import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Ваши вершины
vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0.2, 0.2, 0],
    [0.8, 0.2, 0],
    [0.8, 0.8, 0],
    [0.2, 0.8, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1],
    [0.2, 0.2, 1],
    [0.8, 0.2, 1],
    [0.8, 0.8, 1],
    [0.2, 0.8, 1]
])

# Определение граней для построения выпуклых плоскостей
faces = [
    [0, 1, 5, 4],
    [1, 2, 6, 5],
    [2, 3, 7, 6],
    [3, 0, 4, 7],
    [4, 5, 6, 7],
    [8, 9, 13, 12],
    [9, 10, 14, 13],
    [10, 11, 15, 14],
    [11, 8, 12, 15],
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
    [4, 5],
    [5, 9],
    [6, 10],
    [7, 11],
    [8, 12],
    [9, 10],
    [10, 11],
    [11, 8],
    [12, 13],
    [13, 14],
    [14, 15],
    [15, 12]
]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Отображение выпуклых плоскостей
poly3d = [[vertices[vertex] for vertex in face] for face in faces[:-12]]
ax.add_collection3d(Poly3DCollection(poly3d, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.9))

# Отображение ребер для вырезания отверстия
for i in range(-12, 0):
    ax.plot([vertices[faces[i][0]][0], vertices[faces[i][1]][0]],
            [vertices[faces[i][0]][1], vertices[faces[i][1]][1]],
            [vertices[faces[i][0]][2], vertices[faces[i][1]][2]], color='black')

# Подписи осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

