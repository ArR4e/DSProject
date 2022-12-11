from turtle import *

def ruut(pikkus):
    for i in range(3):
        forward(pikkus)
        left(90)
    forward(pikkus)
    return
        
def fraktal(pikkus, sügavus):
    if sügavus == 1:
        ruut(pikkus)
    else:
        for i in range(3):
            forward(pikkus)
            fraktal(pikkus/2, sügavus-1)
        forward(pikkus)
    return    

fraktal(100,3)
exitonclick()