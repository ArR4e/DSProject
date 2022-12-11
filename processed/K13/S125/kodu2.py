from turtle import *

def fraktal(sügavus, pikkus):
    if sügavus >= 1:
        forward(pikkus)
        left(90)
        fraktal(sügavus-1, 0.5*pikkus)
        left(180)
        forward(pikkus)
        left(90)
        fraktal(sügavus-1, 0.5*pikkus)
        left(180)
        forward(pikkus)
        left(90)
        fraktal(sügavus-1, 0.5*pikkus)
        left(180)
        forward(pikkus)
        right(90)

fraktal(4,100)    