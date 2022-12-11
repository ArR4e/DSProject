from turtle import *

speed(0)

def fraktal(n, length):     
    if n == 1:
        color("red")
        for i in range(4):
            forward(length)
            left(90)
        right(90)
    else:
        color("green")

        forward(length)
        fraktal(n-1, length / 2)
        
        color("brown")

        forward(length)
        fraktal(n-1, length / 2)
        
        color("blue")

        forward(length)
        fraktal(n-1, length / 2)
        
        color("black")
        forward(length)
                 
#fraktal(5, 100)