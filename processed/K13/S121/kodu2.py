from turtle import *

def fun(sügavus, lenght, direction ):
    if sügavus == 0:
        return
    for i in range(3):
        forward(lenght)
        if sügavus > 1:
            lenght= lenght/2
            direction = -direction
            fun(sügavus - 1, lenght, direction)
            direction = -direction
            lenght = lenght*2
        right(direction)
    forward(lenght)
    right(direction)

print(fun(4, 100, 90))