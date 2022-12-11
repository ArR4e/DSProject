from turtle import *

speed(0)

def fraktal(sügavus):
    pikkus =  25*sügavus    
    if sügavus == 1:
        for i in range(4):
            fd(pikkus)
            rt(90)
        lt(90)
    else:
        fd(pikkus)
        for i in range(3):
            fraktal(sügavus-1)
            fd(pikkus)
            
fraktal(4)           
exitonclick()