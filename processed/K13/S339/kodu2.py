from turtle import *

def fraktal(küljepikkus, sügavus):
    if sügavus == 0:
        return
    if sügavus >= 1:
        forward(küljepikkus)
        left(90)
        fraktal(küljepikkus * 0.5, sügavus-1)
        left(180)
        forward(küljepikkus)
        left(90)
        fraktal(küljepikkus * 0.5, sügavus-1)
        left(180)
        forward(küljepikkus)
        left(90)
        fraktal(küljepikkus * 0.5, sügavus-1)
        left(180)
        forward(küljepikkus)
        right(90)