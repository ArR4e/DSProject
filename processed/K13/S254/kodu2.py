from turtle import *

def ruudud(pikkus, sügavus):
    if sügavus <= 0:
        return
    else:
        forward(pikkus)
        ruudud(pikkus*0.5, sügavus-1)
        left(90)
        forward(pikkus)
        ruudud(pikkus*0.5, sügavus-1)
        left(90)
        forward(pikkus)
        ruudud(pikkus*0.5, sügavus-1)
        left(90)
        forward(pikkus)
        left(90)
        right(180)
        
ruudud(100, 4)