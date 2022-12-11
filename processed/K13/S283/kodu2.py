from turtle import *
from turtle import speed

def fraktal(sügavus, pikkus):
    if sügavus <= 0:
        return 0
    else:
        for i in range(4):
            forward(pikkus)
            left(90)
            if sügavus > 1 and i < 3:
                fraktal(sügavus-1, pikkus*0.5)
            left(180)

speed(1000)
fraktal(4,200)
exitonclick()