from turtle import *

def fraktal(tase, pikkus):
    if tase > 1:
        forward(pikkus)
        fraktal(tase-1, pikkus*0.5)
        forward(pikkus)
        fraktal(tase-1, pikkus*0.5)
        forward(pikkus)
        fraktal(tase-1, pikkus*0.5)
        forward(pikkus)
    elif tase == 1:
        forward(pikkus/tase)
        left(90)
        forward(pikkus/tase)
        left(90)
        forward(pikkus/tase)
        left(90)
        forward(pikkus/tase)
        
        
fraktal(3, 100)
exitonclick()