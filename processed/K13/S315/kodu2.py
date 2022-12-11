from turtle import *

def ruut(sügavus, pikkus = 100):
    if sügavus <= 0:
        return
    else:
        forward(pikkus)
        ruut(sügavus-1, pikkus/2)
        right(90)       
        forward(pikkus)
        ruut(sügavus-1, pikkus/2)
        right(90)        
        forward(pikkus)
        ruut(sügavus-1, pikkus/2)
        right(90)
        forward(pikkus)
        left(90)

exitonclick()
        
        
    