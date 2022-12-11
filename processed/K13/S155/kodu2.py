from turtle import *

def fraktal(tase, pikkus):
    if tase == 0:
        right(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        
    elif tase >= 1:
        right(90)
        forward(pikkus)
        fraktal(tase-1, pikkus*0.5)
        right(90)
        forward(pikkus)
        fraktal(tase-1, pikkus*0.5)
        right(90)
        forward(pikkus)
        fraktal(tase-1, pikkus*0.5)
        right(90)
        forward(pikkus)
        
print(fraktal(2,100))
exitonclick()