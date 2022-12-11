from turtle import *
speed(0)

def ruut(sügavus, pikkus):
    if sügavus == 1:
        for i in range(3):
            forward(pikkus)
            right(90)
        forward(pikkus)
    else:
        for i in range(3):
            forward(pikkus)
            left(90)
            ruut(sügavus-1, pikkus*0.5)
            left(90)
        forward(pikkus)
ruut(3, 100)
exitonclick()
