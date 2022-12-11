from turtle import *

def fraktal(tase,pikkus):
    for külg in range(3):
        forward(pikkus)
        if tase > 1:
            fraktal(tase-1,pikkus/2)
        right(90)
    forward(pikkus)
    left(90)

fraktal(4,200)
exitonclick()