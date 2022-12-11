from turtle import *

speed(10)
delay(0)


def fraktal(a, n):
    if n > 0:
        for i in range(4):
            forward(a)
            left(90)
            if i < 3:
                fraktal(a*0.5, n-1)
            left(180)
        
fraktal(100, 4)