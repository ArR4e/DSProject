from turtle import *

def kilpkonn(sügavus, pikkus):
    if sügavus == 0:
        return 0
    elif sügavus == 1:
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
    else:
        kilpkonn(sügavus-1, pikkus-20)
        
        
kilpkonn(3, 100)
