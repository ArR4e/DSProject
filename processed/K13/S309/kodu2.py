from turtle import *

def f(step, length):
    if step >= 1:
        for i in range(4):
            forward(length)
            left(90)
            if i < 3:
                f(step-1, length/2)
                left(180)
        left(180)