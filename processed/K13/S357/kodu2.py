from turtle import *
def fraktal(step, lenght):
    if step > 0:
        for i in range(4):
            forward(lenght)
            left(90)
            if i < 3:
                fraktal(step - 1, 0.5*lenght)
                left(180)
        left(180)