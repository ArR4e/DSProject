from turtle import *

def ruutude_fraktal(ruut, pikkus, nurk):
    for i in range(3):
        fd(pikkus)
        if ruut > 1:
            pikkus = pikkus/2
            nurk = -nurk
            ruutude_fraktal(ruut -1, pikkus, nurk)
            nurk = -nurk
            pikkus *= 2
        right(nurk)
    forward(pikkus)
    right(nurk)
speed(200)
ruutude_fraktal(5, 100, 90)

exitonclick()