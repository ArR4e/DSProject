from turtle import *
def fraktal(tase, pikkus):
    if tase > 0:
        if tase == 1:
            left(90)
            forward(pikkus)
            right(90)
            forward(pikkus)
            right(90)
            forward(pikkus)
            right(90)
            forward(pikkus)
            left(90)
        if tase > 1:
            forward(pikkus)
            fraktal(tase-1, pikkus*0.5)
            forward(pikkus)
            fraktal(tase-1, pikkus*0.5)
            forward(pikkus)
            fraktal(tase-1, pikkus*0.5)
            forward(pikkus)