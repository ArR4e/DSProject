from turtle import *

def fraktal(tase, pikkus):
    if tase == 1:
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
    else:
        forward(pikkus)
        fraktal(tase-1, 0.5 * pikkus)
        forward(pikkus)
        fraktal(tase-1, 0.5 * pikkus)
        forward(pikkus)
        fraktal(tase-1, 0.5 * pikkus)
        forward(pikkus)
        
# fraktal(4, 100)