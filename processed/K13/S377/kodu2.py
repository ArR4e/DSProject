#mirjampirn
from turtle import*

def fraktal(sügavus,pikkus):
    if sügavus== 1:
        for i in range(4):
            forward(pikkus)
            left(90)
            left(180)
    else:
        for i in range(4):
            forward(pikkus)
            left(90)
            if i<3:
                fraktal(sügavus-1,pikkus/2)
            left(180)