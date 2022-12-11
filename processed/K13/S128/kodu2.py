from turtle import *


def fraktal(tase, pikkus):
    if tase >= 1:
        forward(pikkus)
        left(90)
        fraktal(tase-1, pikkus * 0.5)
        right(180)
        forward(pikkus)
        left(90)
        fraktal(tase-1, pikkus * 0.5)
        right(180)
        forward(pikkus)
        left(90)
        fraktal(tase-1, pikkus * 0.5)
        right(180)
        forward(pikkus)
        right(90)
        

fraktal(4, 100)