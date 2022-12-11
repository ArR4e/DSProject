from turtle import *

def fraktal(tase, pikkus, suund =90):
    if tase == 1:
        for i in range(4):
            forward(pikkus)
            left(90)
        
    else:
        for i in range(3):
            forward(pikkus)
            if tase > 1:
                fraktal(tase-1, pikkus/2, -suund)
            right(suund)
        forward(pikkus)
        right(suund)
        
        
    