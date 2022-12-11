from turtle import *

def fraktal (pikkus, n, s):
    if s >= 1:
        if n <= 4:
            forward(pikkus)
            left(90)
            if n <= 3:
                fraktal(pikkus*0.5, 1, s-1)
            left(180)
            fraktal(pikkus, n+1, s)

#delay(0)
#speed(0)
fraktal(100, 1, 1)
exitonclick()

