from turtle import *

def fraktal(pikkus,tase):
    pencolor("MediumSeaGreen")
    speed(50)
    if tase>0:
        forward(pikkus)
        left(90)
        fraktal(pikkus*0.5,tase-1)
        right(180)
        forward(pikkus)
        left(90)
        fraktal(pikkus*0.5,tase-1)
        right(180)
        forward(pikkus)
        left(90)
        fraktal(pikkus*0.5,tase-1)
        right(180)
        forward(pikkus)
        right(90)
        
exitonclick()
        