from turtle import *

def ruut_fraktal(sügavus, pikkus=100, nurk=90, ):
    forward(pikkus)
    for _ in range(3):
        if sügavus > 1:
            ruut_fraktal(sügavus-1, pikkus/2, nurk-2*nurk)
        right(nurk)
        forward(pikkus)
    right(nurk)
