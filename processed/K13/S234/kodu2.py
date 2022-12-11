from turtle import *

def f(sügavus,pikkus):
    if sügavus==1:
        forward(pikkus)
        right(90)
        forward(pikkus)
        right(90)
        forward(pikkus)
        right(90)
        forward(pikkus)
        right(90)
    else:
        forward(pikkus)
        left(90)
        f(sügavus-1,pikkus*0.5)
        right(180)
        forward(pikkus)
        left(90)
        f(sügavus-1,pikkus*0.5)
        right(180)
        forward(pikkus)
        left(90)
        f(sügavus-1,pikkus*0.5)
        right(180)
        forward(pikkus)
        right(90)