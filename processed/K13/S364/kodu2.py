from turtle import *

def fraktal(level, length):
    if level >= 1:
        for i in range(4): #ruut
            forward(length)
            left(90)
            if i < 6:
                fraktal(level - 1, length * 0.5)
            left(180)
fraktal(2, 100)
exitonclick()