from turtle import *

def ruudud(tase, pikkus):
    if tase > 0:
        forward(pikkus)
        left(90)
        ruudud(tase-1, pikkus * 0.5)
        right(180)
        forward(pikkus)
        left(90)
        ruudud(tase-1, pikkus * 0.5)
        right(180)
        forward(pikkus)
        left(90)
        ruudud(tase-1, pikkus * 0.5)
        right(180)
        forward(pikkus)
        right(90)