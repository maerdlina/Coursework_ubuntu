import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-200, 200)
ax.set_ylim(-30, 30)
ax.set_zlim(-0.1, 0.1)

# Открываем файл blockMeshDict
with open('blockMeshDict_number.txt', 'r') as file:
    data = file.read()

# Ищем координаты в файле
import re
pattern = r'\(([-$\w\s.]+)\)//\d+'
matches = re.findall(pattern, data)

two_dimensional_array = [list(map(str.strip, match.split())) for match in matches]
# print(float(two_dimensional_array[8][2]))

# координаты вершин куба
verts = [
    #1 - плоскость
    #[0][0]              #1             #2               #3
    [(0, 18, float(two_dimensional_array[0][2])), (125, 15, float(two_dimensional_array[1][2])), (135, 15, float(two_dimensional_array[2][2])), (150, 18, float(two_dimensional_array[3][2]))],
    #[1][0]
    [(0, 18, float(two_dimensional_array[4][2])), (125, 15, float(two_dimensional_array[5][2])), (135, 15, float(two_dimensional_array[6][2])), (150, 18, float(two_dimensional_array[7][2]))],
    #2 - плоскость
    #[2][0]
    [(0, 0, float(two_dimensional_array[8][2])), (125, 5, float(two_dimensional_array[9][2])), (125, 15, float(two_dimensional_array[10][2])), (0, 18, float(two_dimensional_array[11][2]))],
    #[3][0]
    [(0, 0, float(two_dimensional_array[12][2])), (125, 5, float(two_dimensional_array[13][2])), (125, 15, float(two_dimensional_array[14][2])), (0, 18, float(two_dimensional_array[15][2]))]
]

ax.add_collection3d(Poly3DCollection([verts[0]], facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.7))#низ 1
ax.add_collection3d(Poly3DCollection([verts[1]], facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.7))#верх 1

ax.add_collection3d(Poly3DCollection([verts[2]], facecolors='black', linewidths=1, edgecolors='r', alpha=0.7))#низ 2
ax.add_collection3d(Poly3DCollection([verts[3]], facecolors='black', linewidths=1, edgecolors='r', alpha=0.7))#верх 2

# соединение вершин для боковых плоскостей
side_verts = [
    #1 плоскость
    [verts[0][0], verts[1][0], verts[1][1], verts[0][1]],
    [verts[0][2], verts[1][2], verts[1][3], verts[0][3]],
    [verts[0][1], verts[1][1], verts[1][2], verts[0][2]],
    [verts[0][0], verts[1][0], verts[1][3], verts[0][3]],
    #2 плоскость
    # [verts[0][0], verts[1][0], verts[1][1], verts[0][1]],
    # [verts[0][2], verts[1][2], verts[1][3], verts[0][3]],
    # [verts[0][1], verts[1][1], verts[1][2], verts[0][2]],
    # [verts[0][0], verts[1][0], verts[1][3], verts[0][3]],
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

# # Добавление отображения номеров точек
# for i, txt in enumerate(two_dimensional_array):
#     if(txt[0].isdigit()) and (txt[1].isdigit()):
#         #ax.text(float(txt[0]), '%d' % (i+1), color='black')
#         ax.text(float(txt[0]), float(txt[1]), float(txt[2]), '%d' % (i + 1), size=20, zorder=1, color='k')
#         #print(txt[0], txt[1], txt[2])
#     #print(txt[0])

i = 0
for j in range(0, 10):
    ax.text(float(two_dimensional_array[j][0]), float(two_dimensional_array[j][1]), float(two_dimensional_array[j][2]), '%d' % (i), size=10, zorder=1, color='k')
    ax.scatter(float(two_dimensional_array[j][0]), float(two_dimensional_array[j][1]), float(two_dimensional_array[j][2]), color='b')
    i+=1
for j in range(12, 14):
    ax.text(float(two_dimensional_array[j][0]), float(two_dimensional_array[j][1]), float(two_dimensional_array[j][2]), '%d' % (i), size=20, zorder=1, color='purple')
    ax.scatter(float(two_dimensional_array[j][0]), float(two_dimensional_array[j][1]), float(two_dimensional_array[j][2]), color='b')
    i+=1

plt.show()

# print(two_dimensional_array[0][2])
# Выводим координаты
# for match in matches:
#     print(match)

# flag = True

# def is_float(string):
#   try:
#     flag = True
#     return float(string) and '.' in string  # True if string is a number contains a dot
#   except ValueError:  # String is not a number
#     flag = False
#     return False
#
# for row in two_dimensional_array:
#     for item in row:
#         is_float(item)
#         if item.isdigit() or flag == True:
#             print(f"{item} is a digit")
#         else:
#             print(f"{item} is a text value")