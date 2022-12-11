from turtle import *

speed('fastest')

def fraktal(sygavus, pikkus = 1):
    for i in range(4):
        forward(200 / pikkus)
        left(90)
        if i < 3 and sygavus > 1:
            fraktal(sygavus - 1, pikkus * 2)
        left(180)
            
fraktal(2)
exitonclick()