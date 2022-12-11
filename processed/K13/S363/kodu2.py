from turtle import *


def ruut(sügavus, pikkus):
    #delay(0)
    if sügavus != 1:
        for i in range(3):
            forward(pikkus)
            ruut(sügavus-1, pikkus*0.5)

        forward(pikkus)
        
    else:
        for i in range(4):
            forward(pikkus)
            right(90)
        left(90)
        
    