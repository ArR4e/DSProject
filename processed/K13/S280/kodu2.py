# RP / 2. Sarnaste ruutude fraktal

from turtle import *

speed(0)

def fraktal(pikkus, sügavus):
    sügavus -= 1
    for x in range(4):
        fd(pikkus)
        lt(90)
    if sügavus > 0:
        pikkus = pikkus / 2
        for x in range(3):
            fd(pikkus * 2)
            rt(90)
            fraktal(pikkus, sügavus)
            rt(180)
            if x == 2:
                fd(pikkus * 2)
                lt(90)

fraktal(200,4)
exitonclick()