from turtle import *

def fraktal(sügavus, küljepikkus, keeramisi=2):
    speed(20)
    if sügavus == 1:
        forward(küljepikkus)
        left(90)
        forward(küljepikkus)
        left(90)
        forward(küljepikkus)
        left(90)
        forward(küljepikkus)
        return
    else:
        forward(küljepikkus)
        küljepikkus /= 2
        fraktal(sügavus - 1, küljepikkus)
        küljepikkus *= 2
        if keeramisi == 0:
            forward(küljepikkus)
            return
        fraktal(sügavus, küljepikkus, keeramisi=keeramisi - 1)
                
fraktal(4, 100)
