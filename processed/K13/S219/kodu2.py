from turtle import *

def fraktal(sügavus, pikkus, suund = 90):
    for i in range(3):
        forward(pikkus)
        if sügavus > 1:
            fraktal(sügavus - 1, pikkus / 2, -1 * suund)
        right(suund)
    
    forward(pikkus)
    right(suund)
fraktal(4, 50)