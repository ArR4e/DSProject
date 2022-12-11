from turtle import *

def fraktal(tase, pikkus):
    if tase < 1:
        return
    else:
        for i in range(4):
            forward(pikkus)
            left(90)
            if i < 3:
                fraktal(tase - 1, pikkus//2)
            left(180)

fraktal(2, 100)
exitonclick()
                