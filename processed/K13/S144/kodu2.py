from turtle import *

def fraktal(s,x):
    if s == 0:
        return
    else:
        for i in range(4):
            forward(x)
            left(90)
            if i < 3:
                fraktal(s-1,x/2)
            left(180)
