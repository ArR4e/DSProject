from turtle import *

def fraktal(tase):
    speed(0)
    global pikkus,suund
    for x in range(3):
        forward(pikkus)
        if tase >1:
            pikkus=pikkus/2
            suund=-suund
            fraktal(tase-1)
            suund=-suund
            pikkus=pikkus*2
        right(suund)
    forward(pikkus)
    right(suund)
     
     
pikkus = 100
suund = 90
fraktal(4)
exitonclick()