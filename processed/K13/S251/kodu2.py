from turtle import *

def täisliikumine(pikkus):
    forward(pikkus)
    left(90)
    forward(pikkus)
    left(90)
    forward(pikkus)
    left(90)
    forward(pikkus)
    
def joonis(aste,pikkus):
    if aste == 1:
        täisliikumine(pikkus)
    else:
        for i in range(3):
            forward(pikkus)
            joonis(aste-1,pikkus/2)
        forward(pikkus)

joonis(3,200)
exitonclick()