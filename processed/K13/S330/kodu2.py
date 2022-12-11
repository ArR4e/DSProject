from turtle import *

def fraktal(sügavus, pikkus):
    if sügavus >= 1:
        forward(pikkus)
        fraktal(sügavus-1, pikkus*0.5)
        right(90)
        forward(pikkus)
        fraktal(sügavus-1, pikkus*0.5)
        right(90)
        forward(pikkus)
        fraktal(sügavus-1, pikkus*0.5)
        right(90)
        forward(pikkus)
        left(90)