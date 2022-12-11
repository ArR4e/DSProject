from turtle import *
def fraktal(sügavus, pikkus):
    if sügavus >0:
        for i in range(3):
            forward(pikkus)
            fraktal(sügavus-1, pikkus*0.5)
            if sügavus%2==0:
                left(90)
            else:
                right(90)
        forward(pikkus)
        if sügavus%2==0:
            left(90)
        else:
            right(90)