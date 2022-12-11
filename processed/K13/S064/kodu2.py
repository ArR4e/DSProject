#2. Sarnaste ruutude fraktal

from turtle import *

def fraktal(sügavus):
    global pikkus, suund
    suund = 2
    if sügavus == 1:
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        left(90)
        forward(pikkus)
        return
    else:
        forward(pikkus)
        pikkus /= 2
        fraktal(sügavus - 1)
        pikkus *=2
        if suund == 0:
            forward(pikkus)
            return
        fraktal(sügavus)
    
pikkus = 100
fraktal(3)
exitonclick()