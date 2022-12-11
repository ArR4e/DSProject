from turtle import *

def fraktal(kordus, pikkus):
    if kordus>0:
        for i in range(4):
            forward(pikkus)
            left(90)
            if i < 3:
                fraktal(kordus-1,pikkus*0.5)
            left(180)
fraktal(3,100)
exitonclick()