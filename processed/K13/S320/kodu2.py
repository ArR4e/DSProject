from turtle import *

def fraktal(tase, pikkus):
    if tase == 0:
        return
    if tase % 2 == 0:
        for joon in range(3):
            forward(pikkus)
            fraktal(tase-1, pikkus/2)
            left(90)
        forward(pikkus)
        left(90)
        
    else:
        for joon in range(3):
            forward(pikkus)
            fraktal(tase-1, pikkus/2)
            right(90)
        forward(pikkus)
        right(90)
        

fraktal(3, 100)
