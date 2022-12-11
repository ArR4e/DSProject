from turtle import *

def fraktal(tase, pikkus):
    for i in range(tase):
        if i!=(tase-1):
            forward(pikkus)
            left(90)
            fraktal((tase-1), (pikkus*0.5))
            left(180)
        else:
            for i in range(4):
                forward(25)
                left(90)
                left(180)



fraktal(3, 100)