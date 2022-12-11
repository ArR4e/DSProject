

from turtle import *
global pööre
pööre = 90
speed(0)
def fraktal(pikkus, sügavus):
    
    global pööre
    
    for külg in range(3):
        forward(pikkus)
        
        if sügavus > 1:
            pööre = pööre * (-1)
            fraktal(pikkus/2, sügavus - 1)
            pööre = pööre * (-1)
            
        right(pööre)
    forward(pikkus)
    right(pööre)
    
fraktal(200, 4)

exitonclick()
            