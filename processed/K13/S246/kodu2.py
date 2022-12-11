from turtle import *
def fraktal(sygavus, pikkus):
    if sygavus == 0:
        return 0
    else:
        for i in range(4):
            forward(pikkus)
            left(90)
            if i < 3:
                fraktal(sygavus - 1, pikkus // 2)
            left(180)
        return 0

exitonclick()