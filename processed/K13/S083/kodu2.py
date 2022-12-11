from turtle import *

def fraktal(tase, pikkus, suund=90): 
    for i in range(3):
            forward(pikkus)
            if tase > 1:
                fraktal(tase-1, pikkus/2, -suund)
            right(suund)
    forward(pikkus)
    right(suund)
fraktal(2, 100)

exitonclick()