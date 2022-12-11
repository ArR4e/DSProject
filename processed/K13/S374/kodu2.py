from turtle import *

def fraktal(tase, pikkus):
    hideturtle()
    speed(0)
    if tase == 1:
        for i in range(4):
            forward(pikkus)
            left(90)
            left(180)
    else:
        for i in range(4):
            forward(pikkus)
            left(90)
            if i < 3:
                fraktal(tase-1, pikkus*0.5)
            left(180)

        
        
fraktal(4, 100)
exitonclick()
