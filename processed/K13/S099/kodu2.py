from turtle import *

def fraktal(n, pikkus = 100):
    for i in range(4):
        forward(pikkus)
        left(90)
        if n > 1 and i < 3:
            fraktal(n-1, pikkus/2)
        left(180)
    
        
    
    
fraktal(4)

exitonclick()
    
    