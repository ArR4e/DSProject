from turtle import *
def fraktal(tase):
    global pikkus, suund
    for _ in range(3):
        forward(pikkus)
        if tase > 1:
            pikkus /= 2
            suund = -suund
            fraktal(tase - 1)
            suund = -suund
            pikkus *= 2
        right(suund)
    forward(pikkus)
    right(suund)

pikkus = 100
suund = 90
speed(0)

fraktal(3)
exitonclick()