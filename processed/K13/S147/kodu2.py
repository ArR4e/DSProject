from turtle import *
def fraktal(sügavus):
    for i in range(3):
        forward(50*sügavus)
        if sügavus > 1:
            left(90)
            fraktal(sügavus-1)
        else:
            for i in range(3):
                right(90)
                forward(100/2**sügavus)
            left(90)
            return
    forward(50*sügavus)
    left(90)