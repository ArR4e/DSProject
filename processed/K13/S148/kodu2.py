from turtle import *

def fraktal(x):
    global a, b
    
    for i in range(3):
        forward(a)
        if x > 1:
            a = a / 2
            b = -b
            fraktal(x - 1)
            a = a * 2
            b = -b
        
        right(b)
    
    forward(a)
    right(b)

a = 200
b = 90

exitonclick()