from turtle import *

def frakt(tase, pikkus):
    if tase >= 1:
        fd(pikkus)
        left(90)
        frakt(tase-1, pikkus*0.5)
        left(180)
        fd(pikkus)
        left(90)
        frakt(tase-1, pikkus*0.5)
        left(180)
        fd(pikkus)
        left(90)
        frakt(tase-1, pikkus*0.5)
        left(180)
        fd(pikkus)
        left(90)
        left(180)
exitonclick()