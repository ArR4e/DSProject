from turtle import *

def fraktal(n, pikkus):
    speed(100)
    if n == 1:
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        return
        exitonclick()
    else:
        forward(pikkus)
        right(90)
        fraktal(n-1, pikkus / 2)
        right(90)
        forward(pikkus)
        right(90)
        fraktal(n-1, pikkus / 2)
        right(90)
        forward(pikkus)
        right(90)
        fraktal(n-1, pikkus / 2)
        right(90)
        forward(pikkus)
        
fraktal(2, 50)
