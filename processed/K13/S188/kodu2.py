from turtle import *

def fraktal(tase, pikkus):
    if tase >= 1:
        forward(pikkus)
        fraktal(tase - 1, 0.5*pikkus)
        if tase % 2 == 0:
            right(90)
            forward(pikkus)
            fraktal(tase - 1, 0.5*pikkus)
            right(90)
            forward(pikkus)
            fraktal(tase - 1, 0.5*pikkus)
            right(90)
            forward(pikkus)
            right(90)
        else:
            left(90)
            forward(pikkus)
            fraktal(tase - 1, 0.5*pikkus)
            left(90)
            forward(pikkus)
            fraktal(tase - 1, 0.5*pikkus)
            left(90)
            forward(pikkus)
            left(90)
