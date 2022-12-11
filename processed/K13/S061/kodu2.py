from turtle import *
def fraktaal_ruudust(tase, pikkus):
    if tase >= 1:
        for i in range(4):
            forward(pikkus)
            left(90)
            if i < 3:
                fraktaal_ruudust(tase - 1, pikkus * 0.5)
            left(180)
fraktaal_ruudust(0, 100)
exitonclick()