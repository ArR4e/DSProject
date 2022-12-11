from turtle import *
def fraktal(külje_pikkus, sügavus):
    if sügavus >= 1:
        forward(külje_pikkus)
        fraktal(külje_pikkus/2, sügavus-1)
        lt(90)
        forward(külje_pikkus)
        fraktal(külje_pikkus/2, sügavus-1)
        lt(90)
        forward(külje_pikkus)
        fraktal(külje_pikkus/2, sügavus-1)
        lt(90)
        forward(külje_pikkus)
        rt(90)

fraktal(140, 4)