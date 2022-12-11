from turtle import *

def t(sügavus, külg):
    if sügavus >= 1:
        for i in range(4):
            forward(külg)
            left(90)
            if i < 3:
                t(sügavus - 1, külg / 2)
            left(180)