from turtle import *

def fraktaal(sügavus, külje_pikkus):
    if sügavus == 0:
        return
    elif sügavus == 1:
        for i in range(4):
            forward(külje_pikkus)
            right(90)
    else:
        for i in range(4):
            forward(külje_pikkus)
            left(90)
            if i < 3:
                fraktaal(sügavus-1, külje_pikkus*0.5)
            left(180)