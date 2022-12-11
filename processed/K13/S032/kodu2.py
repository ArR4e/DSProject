from turtle import *

def fraktal(tase, pikkus):
    a=0.5
    tipud = 3
    if tase >=1:
        right(90)
        forward(pikkus)
        for i in range(tipud):
            fraktal(tase-1, a*pikkus)
            left(90)
            forward(pikkus)
        left(90)
        left(90)
    
fraktal(4, 100)    