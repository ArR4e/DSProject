from turtle import *

def joonista(sügavus, pikkus) :
    for i in range(3):
        forward(pikkus)
        if sügavus > 1:
            joonista(sügavus-1, pikkus/2)
        right(90)
    forward(pikkus)
    left(90)
    
#joonista(3, 100)

exitonclick()
