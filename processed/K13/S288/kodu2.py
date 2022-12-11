from turtle import *

def fraktal(sügavus, pikkus, suund):
    for i in range(3):
        forward(pikkus)
        if sügavus > 1:
            pikkus /= 2
            suund = - suund
            fraktal(sügavus - 1, pikkus, suund)
            suund = - suund
            pikkus *= 2
        right(suund)
    forward(pikkus)
    right(suund)

fraktal(4, 100, 90)

hideturtle()
exitonclick()