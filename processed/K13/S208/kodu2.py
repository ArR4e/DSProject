from turtle import *
speed(0)
def ruudud(sügavus, pikkus):
    if sügavus == 0:
        return
    elif sügavus > 0:
        right(90)
        for i in range(4):
            forward(pikkus)
            if i < 3:
                ruudud(sügavus-1, pikkus * 0.5)
            left(90)
        left(90)