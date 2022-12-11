from turtle import *

def fact(samm):
    global pikkus, nurk
    for i in range(3):
        forward(pikkus)
        if samm > 1:
            pikkus /= 2
            nurk = - nurk
            fact(samm -1)
            nurk = - nurk
            pikkus *= 2
        right(nurk)
    forward(pikkus)
    right(nurk)
    speed("fastest")
pikkus = 200
nurk = 90