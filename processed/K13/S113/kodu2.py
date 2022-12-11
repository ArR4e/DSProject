from turtle import *

def fraktal(sügavus, pikkus):
    if sügavus > 1:
        for i in range (3):
            forward(pikkus)
            left(90)
            fraktal(sügavus-1, pikkus / 2)
            left(180)
        forward(pikkus)
        right(90)
        
        
        
        
delay(0)
speed(0)
fraktal(5, 100)
exitonclick()