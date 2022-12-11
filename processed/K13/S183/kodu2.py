from turtle import *
speed(0)
def fraktal(pikkus):
    if pikkus <= 10:
        pass
    else:
        for i in range(4):
            forward(pikkus)
            left(90)
            if i < 3:
                fraktal(pikkus/2)
            left(180)
fraktal(100)
exitonclick()