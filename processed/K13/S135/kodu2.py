from turtle import *
speed(0)
def fraktal(tase, pikkus):
    if tase >= 1:
        for i in range(4):
            forward(pikkus)
            left(90)
            if i < 3:
                fraktal(tase - 1, pikkus * 0.5)
            left(180)