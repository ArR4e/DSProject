from turtle import *

def ruut(tase, pikkus):
    for i in range(3):
        forward(pikkus)
        if tase > 1:
            ruut(tase-1, pikkus/2)
        left(90)
    forward(pikkus)
    right(90)

exitonclick()
    