from turtle import *

def fraktal(n, side=100, sides=1):
    forward(side)
    if n == 1 and sides < 4:
        right(90)
        fraktal(n, side, sides+1)
    if n > 1 and sides < 4:
        left(90)
        fraktal(n-1, side/2)
        left(90)
        fraktal(n, side, sides+1)
        
speed(10)

fraktal(5)

exitonclick()