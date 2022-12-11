from turtle import *

speed(0)
def fraktal(sügavus, pikkus):
    if sügavus >= 1:
        forward(pikkus)
        right(90)
        fraktal(sügavus-1, pikkus/2)
        right(180)
        forward(pikkus)
        right(90)
        fraktal(sügavus-1, pikkus/2)
        right(180)
        forward(pikkus)
        right(90)
        fraktal(sügavus-1, pikkus/2)
        right(180)
        forward(pikkus)
        right(90)
        right(180)
fraktal(5, 100)        
exitonclick()