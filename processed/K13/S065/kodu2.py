from turtle import *

def fraktal(ruut, pikkus, nurk):
    for i in range(3):
        forward(pikkus)
        
        if ruut > 1:
            pikkus = pikkus/2
            nurk = -nurk
            fraktal(ruut - 1, pikkus, nurk)
            nurk = -nurk
            pikkus *= 2
        right(nurk)
    
    forward(pikkus)
    right(nurk)

fraktal(2, 100, 90)
exitonclick()