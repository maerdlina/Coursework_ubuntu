import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import TextBox
from matplotlib.widgets import Button
from io import *
from subprocess import *
import os
import math
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-200, 200)
ax.set_ylim(-30, 30)
ax.set_zlim(-0.4, 0.4)

# Открываем файл blockMeshDict
with open('blockMeshDict_number.txt', 'r') as file:
    data = file.read()

# Ищем координаты в файле
import re
pattern = r'\(([-$\w\s.]+)\)//\d+'
matches = re.findall(pattern, data)
two_dimensional_array = [list(map(str.strip, match.split())) for match in matches]

# for i in range(15):
#     if(two_dimensional_array[i][1].isdigit()):
#         print("digital")

def visualizeGraph(expr):
    ax.clear()

    #fground = 0.7
    fground = float(fground_btn.text)
    ax.set_xlim(-30, 200)
    ax.set_ylim(-25, 50)
    ax.set_zlim(-0.4, 0.4)

    intlet_const = 18
    outlet_const = 30

    inlet_m = float(inlet.text)
    outlet_m = float(outlet.text)

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
        [(0, 0, float(two_dimensional_array[20][2])),  # 20  = verts[5][0]
         (150, 0, float(two_dimensional_array[21][2])),  # 21 = verts[5][1]
         (135, 5, float(two_dimensional_array[22][2])),  # 22 = verts[5][2]
         (125, 5, float(two_dimensional_array[23][2]))],  # 23 = verts[5][3]
        #4 [6][0] -0.1-----------------------------------------------------------
        [(135, 5, float(two_dimensional_array[24][2])),  # 24  = verts[6][0]
         (150, 0, float(two_dimensional_array[25][2])),  # 25 = verts[6][1]
         (150, float(inlet.text), float(two_dimensional_array[26][2])),  # 26 = verts[6][2]
         (135, 15, float(two_dimensional_array[27][2]))],  # 27 = verts[6][3]
        # [7][0] 0.1
        [(135, 5, float(two_dimensional_array[28][2])),  # 28  = verts[7][0]
         (150, 0, float(two_dimensional_array[29][2])),  # 29 = verts[7][1]
         (150, float(inlet.text), float(two_dimensional_array[30][2])),  # 30 = verts[7][2]
         (135, 15, float(two_dimensional_array[31][2]))],  # 31 = verts[7][3]
        # 5 [8][0] -0.1-----------------------------------------------------------
        [(125, 8, float(two_dimensional_array[32][2])),  # 32  = verts[8][0]
         (135, 8, float(two_dimensional_array[33][2])),  # 33 = verts[8][1]
         (135, 12, float(two_dimensional_array[34][2])),  # 34 = verts[8][2]
         (125, 12, float(two_dimensional_array[35][2]))],  # 35 = verts[8][3]
        # [9][0] 0.1
        [(125, 8, float(two_dimensional_array[36][2])),  # 36  = verts[9][0]
         (135, 8, float(two_dimensional_array[37][2])),  # 37 = verts[9][1]
         (135, 12, float(two_dimensional_array[38][2])),  # 38 = verts[9][2]
         (125, 12, float(two_dimensional_array[39][2]))],  # 39 = verts[9][3]
        # 6 [10][0] -0.1-----------------------------------------------------------
        [(150, 0, float(two_dimensional_array[40][2])),  # 40  = verts[10][0]
         (180, 0, float(two_dimensional_array[41][2])),  # 41 = verts[10][1]
         (180, float(inlet.text), float(two_dimensional_array[42][2])),  # 42 = verts[10][2]
         (150, float(inlet.text), float(two_dimensional_array[43][2]))],  # 43 = verts[10][3]
        # [11][0] 0.1
        [(150, 0, float(two_dimensional_array[44][2])),  # 44  = verts[11][0]
         (180, 0, float(two_dimensional_array[45][2])),  # 45 = verts[11][1]
         (180, float(inlet.text), float(two_dimensional_array[46][2])),  # 46 = verts[11][2]
         (150, float(inlet.text), float(two_dimensional_array[47][2]))],  # 47 = verts[11][3]
        # 7 [10][0] -0.1-----------------------------------------------------------
        [(150, float(inlet.text), float(two_dimensional_array[48][2])),  # 48  = verts[12][0]
         (180, float(inlet.text), float(two_dimensional_array[49][2])),  # 49 = verts[12][1]
         (180, outlet_m, float(two_dimensional_array[50][2])),  # 50 = verts[12][2]
         (150, outlet_m, float(two_dimensional_array[51][2]))],  # 51 = verts[12][3]
        # [11][0] 0.1
        [(150, float(inlet.text), float(two_dimensional_array[52][2])),  # 52  = verts[13][0]
         (180, float(inlet.text), float(two_dimensional_array[53][2])),  # 53 = verts[13][1]
         (180, outlet_m, float(two_dimensional_array[54][2])),  # 54  = verts[13][2]
         (150, outlet_m, float(two_dimensional_array[55][2]))],  # 55 = verts[13][3]
        #+(abs(intlet_const - float(inlet.text)))
    ]

    for i in range(0, 2):
        ax.add_collection3d(
            Poly3DCollection([verts[i]], facecolors='white', linewidths=1, edgecolors='r', alpha=fground))  # верх-низ 1
    for i in range(2, 4):
        ax.add_collection3d(
            Poly3DCollection([verts[i]], facecolors='blue', linewidths=1, edgecolors='r', alpha=fground))  # верх-низ 2
    for i in range(4, 6):
        ax.add_collection3d(
            Poly3DCollection([verts[i]], facecolors='red', linewidths=1, edgecolors='r', alpha=fground))  # верх-низ 3
    for i in range(6, 8):
        ax.add_collection3d(
            Poly3DCollection([verts[i]], facecolors='green', linewidths=1, edgecolors='r', alpha=fground))  # верх-низ 4
    for i in range(8, 10):#серединка
        ax.add_collection3d(
            Poly3DCollection([verts[i]], facecolors='black', linewidths=1, edgecolors='r', alpha=fground))  # верх-низ 4
    for i in range(10, 12):
        ax.add_collection3d(
            Poly3DCollection([verts[i]], facecolors='white', linewidths=1, edgecolors='r', alpha=fground))  # верх-низ 4
    for i in range(12, 14):
        ax.add_collection3d(
            Poly3DCollection([verts[i]], facecolors='red', linewidths=1, edgecolors='r', alpha=fground))  # верх-низ 4
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
        # 3 плоскость
        [verts[4][0], verts[5][0], verts[5][1], verts[4][1]],  # new 2.1
        [verts[4][1], verts[5][1], verts[5][2], verts[4][2]],  # new 2.2 +
        #[verts[2][0], verts[3][0], verts[3][1], verts[2][1]],  # new 2.3 +
        # 4 плоскость
        [verts[8][0], verts[9][0], verts[9][1], verts[8][1]],  # new 2.1
        [verts[8][3], verts[9][3], verts[9][2], verts[8][2]],  # new 2.2 +
        # 5 плоскость
        [verts[6][0], verts[7][0], verts[7][3], verts[6][3]],  # new 2.1
        [verts[6][1], verts[7][1], verts[7][2], verts[6][2]],  # new 2.2 +
        # 6 плоскость
        [verts[10][0], verts[11][0], verts[11][1], verts[10][1]],  # new 2.1
        [verts[10][1], verts[11][1], verts[11][2], verts[10][2]],  # new 2.2 +
        [verts[10][3], verts[11][3], verts[11][2], verts[10][2]],  # new 2.2 +
        # 7 плоскость
        [verts[12][1], verts[13][1], verts[13][2], verts[12][2]],  # new 2.1
        [verts[12][2], verts[13][2], verts[13][3], verts[12][3]],  # new 2.2 +
        [verts[12][3], verts[13][3], verts[13][0], verts[12][0]],  # new 2.2 +
    ]

    # отображение боковых плоскостей
    # 1 - плокскость

    for i in range(0, 4):
        ax.add_collection3d(Poly3DCollection([side_verts[i]], facecolors='white', linewidths=1, edgecolors='r', alpha=fground))

    for i in range(4, 7):
        ax.add_collection3d(Poly3DCollection([side_verts[i]], facecolors='blue', linewidths=1, edgecolors='r', alpha=fground))

    for i in range(7, 9):
        ax.add_collection3d(Poly3DCollection([side_verts[i]], facecolors='red', linewidths=1, edgecolors='r', alpha=fground))

    for i in range(9, 11):
        ax.add_collection3d(Poly3DCollection([side_verts[i]], facecolors='black', linewidths=1, edgecolors='r', alpha=fground))

    for i in range(11, 13):
        ax.add_collection3d(Poly3DCollection([side_verts[i]], facecolors='green', linewidths=1, edgecolors='r', alpha=fground))

    for i in range(13, 16):
        ax.add_collection3d(Poly3DCollection([side_verts[i]], facecolors='white', linewidths=1, edgecolors='r', alpha=fground))

    for i in range(16, 19):
        ax.add_collection3d(Poly3DCollection([side_verts[i]], facecolors='red', linewidths=1, edgecolors='r', alpha=fground))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

#     text = FoamFile
# {
#     format      ascii;
#     class       dictionary;
#     object      blockMeshDict;
# }
# // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
#
# convertToMeters 0.1;
#
# inlet_const 18;
# outlet_const 30;
#
# p_xf_r_1_const 125;
# p_xs_r_1_const 135;
# p_xf_r_2_const 125;
# p_xs_r_2_const 135;
#
# inlet 25;
# outlet_y 60;
#
# move_xf_rect_1 40;
# move_xs_rect_1 40;
# move_xf_rect_2 40;
# move_xs_rect_2 40;
#
# p_xf_r_1 #calc "$p_xf_r_1_const - $move_xf_rect_1";//1 rect 125 - move
# p_xs_r_1 #calc "$p_xs_r_1_const - $move_xs_rect_1";//2 rect 125 - move
# p_xf_r_2 #calc "$p_xf_r_2_const - $move_xf_rect_2";//1 rect 135 - move
# p_xs_r_2 #calc "$p_xs_r_2_const - $move_xs_rect_2";//2 rect 135 - move
#
# vertices
# (
#     //first - verh
#     (0 $inlet -0.1)//0
#     ($p_xf_r_1 15 -0.1)//1
#     ($p_xs_r_1 15 -0.1)//2
#     (150 $inlet -0.1)//3
#     (0 $inlet 0.1)//4
#     ($p_xf_r_1 15 0.1)//5
#     ($p_xs_r_1 15 0.1)//6
#     (150 $inlet 0.1)//7
#     //second - left bock
#     (0 0 -0.1)//8
#     ($p_xf_r_2 5 -0.1)//9
#     ($p_xf_r_1 15 -0.1)//10
#     (0 $inlet -0.1)//11
#     (0 0 0.1)//12
#     ($p_xf_r_2 5 0.1)//13
#     ($p_xf_r_1 15 0.1)//14
#     (0 $inlet 0.1)//15
#     //third - niz
#     (0 0 -0.1)//16
#     (150 0 -0.1)//17
#     ($p_xs_r_2 5 -0.1)//18
#     ($p_xf_r_2 5 -0.1)//19
#     (0 0 0.1)//20
#     (150 0 0.1)//21
#     ($p_xs_r_2 5 0.1)//22
#     ($p_xf_r_2 5 0.1)//23
#      //four - right bok
#      ($p_xs_r_2 5 -0.1)//24
#      (150 0 -0.1)//25
#      (150 $inlet -0.1)//26
#      ($p_xs_r_2 15 -0.1)//27
#      ($p_xs_r_2 5 0.1)//28
#      (150 0 0.1)//29
#      (150 $inlet 0.1)//30
#      ($p_xs_r_2 15 0.10)//31
#     //five - rectangle mesh center mezdu rectangle
#     ($p_xf_r_2 8 -0.1)//32
#     ($p_xs_r_2 8 -0.1)//33
#     ($p_xs_r_1 12 -0.1)//34
#     ($p_xf_r_1 12 -0.1)//35
#     ($p_xf_r_2 8 0.1)//36
#     ($p_xs_r_2 8 0.1)//37
#     ($p_xs_r_1 12 0.1)//38
#     ($p_xf_r_1 12 0.1)//39
#     //six - nizn firt rectangle
#     (150 0 -0.1)//40
#     (180 0 -0.1)//41
#     (180 $inlet -0.1)//42
#     (150 $inlet -0.1)//43
#     (150 0 0.1)//44
#     (180 0 0.1)//45
#     (180 $inlet 0.1)//46
#     (150 $inlet 0.1)//47
#     //seven - verhn posl recatngle
#     (150 $inlet -0.1)//48
#     (180 $inlet -0.1)//49
#     (180 $outlet_y -0.1)//50
#     (150 $outlet_y -0.1)//51
#     (150 $inlet 0.1)//52
#     (180 $inlet 0.1)//53
#     (180 $outlet_y 0.1)//54
#     (150 $outlet_y 0.1)//55
# );
#
# blocks
# (
#     hex (0 1 2 3 4 5 6 7) (20 20 1) simpleGrading (1 1 1)
#     hex (8 9 10 11 12 13 14 15) (20 20 1) simpleGrading (1 1 1)
#     hex (16 17 18 19 20 21 22 23) (20 20 1) simpleGrading (1 1 1)
#     hex (24 25 26 27 28 29 30 31) (20 20 1) simpleGrading (1 1 1)
#     hex (32 33 34 35 36 37 38 39) (20 20 1) simpleGrading (1 1 1)
#     hex (40 41 42 43 44 45 46 47) (20 20 1) simpleGrading (1 1 1)
#     hex (48 49 50 51 52 53 54 55) (20 20 1) simpleGrading (1 1 1)
# );
#
# boundary
# (
#     inlet
#     {
#         type patch;
#         faces
#         (
#             (8 12 11 15)
#         );
#     }
#
#     outlet
#     {
#         type patch;
#         faces
#         (
#             (41 45 46 42)
#             (49 53 54 50)
#         );
#     }
#
#     frontAndBack
#     {
#         type empty;
#         faces
#         (
#         (0 1 2 3)
#         (4 5 6 7)
#         (8 9 10 11)
#         (12 13 14 15)
#         (16 17 18 19)
#         (20 21 22 23)
#         (24 25 26 27)
#         (28 29 30 31)
#         (32 33 34 35)
#         (36 37 38 39)
#         (40 41 42 43)
#         (44 45 46 47)
#         (48 49 50 51)
#         (52 53 54 55)
#         );
#     }
#
#     topAndBottom
#     {
#         type wall;
#         faces
#         (
#         //top
#             (0 4 7 3)
#             (48 52 55 51)
#             (51 55 54 50)
#         //bottom
#             (16 20 21 17)
#             (40 44 45 41)
#         );
#     }
# );

    text = f"""{inlet_m}"""
    text_format_file = """FoamFile
{
    format      ascii;
    class       dictionary;
    object      blockMeshDict;
}

convertToMeters 0.1;

vertices
(
"""
    text_param = f"""\t({two_dimensional_array[0][0]} {inlet_m} {two_dimensional_array[0][2]})//0
    ({two_dimensional_array[1][0]} {two_dimensional_array[1][1]} {two_dimensional_array[1][2]})//1
    ({two_dimensional_array[2][0]} {two_dimensional_array[2][1]} {two_dimensional_array[2][2]})//2
    ({two_dimensional_array[3][0]} {inlet_m} {two_dimensional_array[3][2]})//3
    ({two_dimensional_array[4][0]} {inlet_m} {two_dimensional_array[4][2]})//0
    ({two_dimensional_array[5][0]} {two_dimensional_array[5][1]} {two_dimensional_array[5][2]})//1
    ({two_dimensional_array[6][0]} {two_dimensional_array[6][1]} {two_dimensional_array[6][2]})//2
    ({two_dimensional_array[7][0]} {inlet_m} {two_dimensional_array[7][2]})//3
);
"""
    with open('blockMeshDict_new', 'w+') as file:
        file.write(text_format_file+text_param)
        file.close()

    plt.draw()
    #os.system('cmd')
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

axbox3 = fig.add_axes([0.1, 0.6, 0.1, 0.040])
outlet = TextBox(axbox3, "outlet", textalignment="center")
outlet.set_val(30)  # Trigger `submit` with the initial string.

axbox4 = fig.add_axes([0.1, 0.5, 0.1, 0.040])
fground_btn = TextBox(axbox4, "foreground", textalignment="center")
fground_btn.set_val(0.7)  # Trigger `submit` with the initial string.

ax_button = plt.axes([0.1, 0.4, 0.1, 0.08])
button = Button(ax_button, 'Обновить')
button.on_clicked(visualizeGraph)

Popen("cmd /k dir")

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