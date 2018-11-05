# coding:utf-8
from matplotlib import pyplot as plt
import numpy as np

file_name = 'mouse_log.txt'

# 获取轨迹坐标    x,y
def get_x_y_datas():
    x = []
    y = []
    x_max = 1
    y_max = 1
    with open(file_name) as f:
        lines = f.readlines()
        for  line in lines:
            _x, _y = line.split(' ')
            _x = int(_x)
            _y = int(_y)

            if _x > x_max:
                x_max = _x
            if _y >y_max:
                y_max = _y
            x.append(int(_x))
            y.append(int(_y))
    x_max = float(x_max)
    y_max = float(y_max)
    a = map(lambda t: t / x_max, x)
    b = map(lambda t: (y_max - t) / y_max, y)
    # a = [0.5,0.6,]
    # b = [0.23,^]
    return a, b

def scatter(x, y):
    ''' 绘制散点图
    :param x: X 坐标集合
    :param y: Y 坐标集合
    :return:
    '''
    # 画布
    plt.figure(figsize=(10, 8))

    # 颜色
    plot_color = np.arctan2(x, y)

    # c颜色
    plt.scatter(x, y, c=plot_color, s=25, alpha=1, marker='o')
    plt.show()

# x,y坐标  列表
mouse_x, mouse_y = get_x_y_datas()
scatter(mouse_x, mouse_y)