from turtle import *

def fraktal(sügavus, pikkus):
    if sügavus < 1:
        return
    else:
        for i in range(4):
            forward(pikkus)
            if i < 3:
                fraktal(sügavus - 1, pikkus // 2)
            left(90)
        left(180)
        
fraktal(3, 100)
exitonclick()
                