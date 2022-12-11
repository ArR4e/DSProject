from turtle import *

def fraktal(x):
    global pikkus
    global kraadid
    for i in range(3):
        forward(pikkus)
        if x > 1:
            pikkus = pikkus / 2
            kraadid = - kraadid
            fraktal(x - 1)
            kraadid = - kraadid
            pikkus *= 2
        right(kraadid)
    forward(pikkus)
    right(kraadid)
            

pikkus = 100
kraadid = 90

exitonclick()