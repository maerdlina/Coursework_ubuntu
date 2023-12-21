import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import TextBox
from matplotlib.widgets import Button
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-200, 200)
ax.set_ylim(-30, 30)
ax.set_zlim(-0.4, 0.4)

# Открываем файл blockMeshDict
with open('blockMeshDict', 'r') as file:
    data = file.read()

# Ищем координаты в файле
import re
pattern = r'\(([-$\w\s.]+)\)//\d+'
matches = re.findall(pattern, data)

two_dimensional_array = [list(map(str.strip, match.split())) for match in matches]
for i in range(15):
    if(two_dimensional_array[i][1].isdigit()):
        print("digital")

def visualizeGraph(expr):
    ax.clear()

    ax.set_xlim(-200, 200)
    ax.set_ylim(-30, 30)
    ax.set_zlim(-0.4, 0.4)

    verts = [
        # 1 - плоскость
        # [0][0]              #1             #2               #3 - 0.1
        [(0, float(inlet.text), float(two_dimensional_array[0][2])),  # 0 = verts[0][0]
         (125, 15, float(two_dimensional_array[1][2])),  # 1 = verts[0][1]
         (135, 15, float(two_dimensional_array[2][2])),  # 2 = verts[0][2]
         (150, float(inlet.text), float(two_dimensional_array[3][2]))],  # 3 = verts[0][3]
        # [1][0] 0.1
        [(0, float(inlet.text), float(two_dimensional_array[4][2])),  # 4 = verts[1][0]
         (125, 15, float(two_dimensional_array[5][2])),  # 5 = verts[1][1]
         (135, 15, float(two_dimensional_array[6][2])),  # 6 = verts[1][2]
         (150, float(inlet.text), float(two_dimensional_array[7][2]))],  # 7 = verts[1][3]
        # 2 - плоскость --------------------------------------------------------------------------------
        # [2][0] -0.1
        [(0, 0, float(two_dimensional_array[8][2])),  # 8  = verts[2][0]
         (125, 5, float(two_dimensional_array[9][2])),  # 9 = verts[2][1]
         (125, 15, float(two_dimensional_array[10][2])),  # 10 - 1 = verts[2][2]
         (0, float(inlet.text), float(two_dimensional_array[11][2]))],  # 11 - 0 = verts[2][3]
        # [3][0] 0.1
        [(0, 0, float(two_dimensional_array[12][2])),  # 12  = verts[3][0]
         (125, 5, float(two_dimensional_array[13][2])),  # 13 = verts[3][1]
         (125, 15, float(two_dimensional_array[14][2])),  # 14 - 5 = verts[3][2]
         (0, float(inlet.text), float(two_dimensional_array[15][2]))],#15 - 4 = verts[3][3]
        #3 - плоскость----------------------------------------------------------------------------------------------
        # [4][0] -0.1
        [(0, 0, float(two_dimensional_array[16][2])),  # 16  = verts[4][0]
         (150, 0, float(two_dimensional_array[17][2])),  # 17 = verts[4][1]
         (135, 5, float(two_dimensional_array[18][2])),  # 18 = verts[4][2]
         (125, 5, float(two_dimensional_array[19][2]))],  # 19 = verts[4][3]
        # [5][0] 0.1
        [(0, 0, float(two_dimensional_array[20][2])),  # 20  = verts[3][0]
         (150, 0, float(two_dimensional_array[21][2])),  # 21 = verts[3][1]
         (135, 5, float(two_dimensional_array[22][2])),  # 22 - 5 = verts[3][2]
         (125, 5, float(two_dimensional_array[23][2]))],  # 23 - 4 = verts[3][3]

    ]

    for i in range(0, 2):
        ax.add_collection3d(
            Poly3DCollection([verts[i]], facecolors='black', linewidths=1, edgecolors='r', alpha=0.7))  # верх-низ 1
    for i in range(2, 4):
        ax.add_collection3d(
            Poly3DCollection([verts[i]], facecolors='purple', linewidths=1, edgecolors='r', alpha=0.7))  # верх-низ 2
    for i in range(4, 6):
        ax.add_collection3d(
            Poly3DCollection([verts[i]], facecolors='blue', linewidths=1, edgecolors='r', alpha=0.7))  # верх-низ 2

    # соединение вершин для боковых плоскостей
    side_verts = [
        # 1 плоскость
        [verts[0][0], verts[1][0], verts[1][1], verts[0][1]], #1.1
        [verts[0][2], verts[1][2], verts[1][3], verts[0][3]], #1.2
        [verts[0][1], verts[1][1], verts[1][2], verts[0][2]], #1.3
        [verts[0][0], verts[1][0], verts[1][3], verts[0][3]], #1.4
        # 2 плоскость
        [verts[2][3], verts[3][3], verts[3][0], verts[2][0]], # new 2.1
        #[verts[3][3], verts[3][2], verts[2][2], verts[2][3]], # - тажа плоскость что и 1.1
        [verts[2][2], verts[2][1], verts[3][1], verts[3][2]], # new 2.2 +
        [verts[2][0], verts[3][0], verts[3][1], verts[2][1]],  # new 2.3 +
    ]

    # отображение боковых плоскостей
    # 1 - плокскость

    for i in range(0, 4):
        ax.add_collection3d(Poly3DCollection([side_verts[i]], facecolors='black', linewidths=1, edgecolors='r', alpha=0.7))

    for i in range(4, 7):
        ax.add_collection3d(Poly3DCollection([side_verts[i]], facecolors='purple', linewidths=1, edgecolors='r', alpha=0.7))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    #number_points()

    #print(len(two_dimensional_array)) - 56

    print(inlet.text)
    plt.draw()
#
axbox = fig.add_axes([0.1, 0.9, 0.1, 0.040])
inlet = TextBox(axbox, "Inlet", textalignment="center")
inlet.set_val(18)  # Trigger `submit` with the initial string.

axbox1 = fig.add_axes([0.1, 0.8, 0.1, 0.040])
rectangle_x_1 = TextBox(axbox1, "x1", textalignment="center")
rectangle_x_1.set_val(135)  # Trigger `submit` with the initial string.

axbox2 = fig.add_axes([0.1, 0.7, 0.1, 0.040])
rectangle_x_2 = TextBox(axbox2, "x2", textalignment="center")
rectangle_x_2.set_val(125)  # Trigger `submit` with the initial string.

ax_button = plt.axes([0.1, 0.6, 0.1, 0.08])
button = Button(ax_button, 'Обновить')
button.on_clicked(visualizeGraph)
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

#-----------------------------------------------------------------------------------------------------------------------

# # Добавление отображения номеров точек
    # for i, txt in enumerate(two_dimensional_array):
    #     if(txt[0].isdigit()) and (txt[1].isdigit()):
    #         #ax.text(float(txt[0]), '%d' % (i+1), color='black')
    #         ax.text(float(txt[0]), float(txt[1]), float(txt[2]), '%d' % (i + 1), size=20, zorder=1, color='k')
    #         #print(txt[0], txt[1], txt[2])
    #     #print(txt[0])

    # i = 0
    # for j in range(0, 10):
    #     ax.text(float(two_dimensional_array[j][0]), float(two_dimensional_array[j][1]),
    #             float(two_dimensional_array[j][2]), '%d' % (i), size=10, zorder=1, color='k')
    #     # ax.scatter(float(two_dimensional_array[j][0]), float(two_dimensional_array[j][1]), float(two_dimensional_array[j][2]), color='b')
    #     i += 1
    # for j in range(12, 14):
    #     ax.text(float(two_dimensional_array[j][0]), float(two_dimensional_array[j][1]),
    #             float(two_dimensional_array[j][2]), '%d' % (i), size=20, zorder=1, color='purple')
    #     # ax.scatter(float(two_dimensional_array[j][0]), float(two_dimensional_array[j][1]), float(two_dimensional_array[j][2]), color='b')
    #     i += 1


# print(float(two_dimensional_array[8][2]))

# координаты вершин куба

# def number_points():
#     number = 0
#     #index = 0
#     for index in range(0, 8):
#         ax.text(float(two_dimensional_array[index][0]), float(two_dimensional_array[index][1]),
#                 float(two_dimensional_array[index][2]), index, size=6, zorder=2, color='blue')
#         ax.scatter(float(two_dimensional_array[index][0]), float(two_dimensional_array[index][1]),
#                 float(two_dimensional_array[index][2]), color='b')