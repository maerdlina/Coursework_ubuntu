import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-200, 200)
ax.set_ylim(-30, 30)
ax.set_zlim(-0.1, 0.1)

# координаты вершин куба
verts = [
    #1 - плоскость
    #[0][0]              #1             #2               #3
    [(0, 18, -0.1), (125, 15, -0.1), (135, 15, -0.1), (150, 18, -0.1)],
    #[1][0]
    [(0, 18, 0.1), (125, 15, 0.10), (135, 15, 0.10), (150, 18, 0.10)],
    #2 - плоскость
    [(0, 0, -0.1), (125, 5, -0.1), (125, 15, -0.1), (0, 18, -0.1)],
    [(0, 0, 0.1), (125, 5, 0.1), (125, 15, 0.1), (0, 18, 0.1)]
]

ax.add_collection3d(Poly3DCollection([verts[0]], facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.7))
ax.add_collection3d(Poly3DCollection([verts[1]], facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.7))

ax.add_collection3d(Poly3DCollection([verts[2]], facecolors='black', linewidths=1, edgecolors='r', alpha=0.7))
ax.add_collection3d(Poly3DCollection([verts[3]], facecolors='black', linewidths=1, edgecolors='r', alpha=0.7))

# соединение вершин для боковых плоскостей
side_verts = [
    #1 плоскость
    [verts[0][0], verts[1][0], verts[1][1], verts[0][1]],
    [verts[0][2], verts[1][2], verts[1][3], verts[0][3]],
    [verts[0][1], verts[1][1], verts[1][2], verts[0][2]],
    [verts[0][0], verts[1][0], verts[1][3], verts[0][3]]
]

# отображение боковых плоскостей
#1 - плокскость
ax.add_collection3d(Poly3DCollection([side_verts[0]], facecolors='black', linewidths=1, edgecolors='r', alpha=0.7))
ax.add_collection3d(Poly3DCollection([side_verts[1]], facecolors='green', linewidths=1, edgecolors='r', alpha=0.7))
ax.add_collection3d(Poly3DCollection([side_verts[2]], facecolors='purple', linewidths=1, edgecolors='r', alpha=0.7))
ax.add_collection3d(Poly3DCollection([side_verts[3]], facecolors='yellow', linewidths=1, edgecolors='r', alpha=0.7))

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Открываем файл blockMeshDict
with open('blockMeshDict', 'r') as file:
    data = file.read()

# Ищем координаты в файле
import re
pattern = r'\(([-$\w\s.]+)\)//\d+'
matches = re.findall(pattern, data)

two_dimensional_array = [list(map(str.strip, match.split())) for match in matches]

# print(two_dimensional_array[0][2])
# Выводим координаты
# for match in matches:
#     print(match)

flag = True

def is_float(string):
  try:
    flag = True
    return float(string) and '.' in string  # True if string is a number contains a dot
  except ValueError:  # String is not a number
    flag = False
    return False

for row in two_dimensional_array:
    for item in row:
        is_float(item)
        if item.isdigit() or flag == True:
            print(f"{item} is a digit")
        else:
            print(f"{item} is a text value")

plt.show()
