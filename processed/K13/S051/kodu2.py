from turtle import *

def fraktal(sügavus, pikkus=100):
    if sügavus > 0:
        pensize(2)
        right(90)
        for i in range(3):
            forward(pikkus)
            fraktal(sügavus-1, pikkus//2)
            left(90)
        forward(pikkus)
        right(180)