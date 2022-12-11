from turtle import *

speed(-1)
def fraktal(tase, pikkus):
    if tase == 1:
        for i in range(4):
            forward(pikkus)
            right(90)
    else:
        for i in range(4):
            forward(pikkus)
            right(90)
            right(180)
            fraktal(tase-1, pikkus*0.4)
            right(180)
    
        
        
fraktal(3, 100)