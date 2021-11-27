import cv2
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt

xmin = int(input('Х мин '))
xmax = int(input('Х макс '))
xStep = int(input('Х шаг '))
k = int(input('K '))
b = int(input('B '))
if b != 0 or xmin != 0:
    x = xmin
    listx = [[], []]
    listy = [[], []]
    while x < xmax:
        y = b + (x * x + k)
        listy[0].append(y)
        listx[0].append(x)
        x += xStep
    plt.plot(listx[0], listy[0], linewidth=3)

    plt.savefig('10.png', bbox_inches="tight")
    plt.show()
    plt.close("all")