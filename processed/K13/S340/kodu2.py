from turtle import *

def ruudud(sügavus,pikkus):
    if sügavus>=1:
        right(90)
        forward(pikkus)
        ruudud(sügavus-1,pikkus/2)
        left(90)
        forward(pikkus)
        ruudud(sügavus-1,pikkus/2)
        left(90)
        forward(pikkus)
        ruudud(sügavus-1,pikkus/2)
        left(90)
        forward(pikkus)
        left(180)
ruudud(1,100)