from turtle import *
def fraktaal(tase, pikkus):
    if tase >= 1:
        for i in range(4):
            forward(pikkus)
            left(90)
            if i < 3:
                fraktaal(tase - 1, pikkus * 0.5)
            left(180)
fraktaal(3, 100)
exitonclick()