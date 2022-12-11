from turtle import *

def fraktal(n, pikkus=100):
    
    for i in range(3):
        forward(pikkus)

        if n > 1:
            fraktal(n - 1, pikkus / 2)
            left(180)
        
        left(90)

    forward(pikkus)
    left(90)

exitonclick()