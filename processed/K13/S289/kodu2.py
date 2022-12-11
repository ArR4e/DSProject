from turtle import *

def ruutude_fraktal(sügavus):
    global pikkus, suund
    
    for i in range(3):
        forward(pikkus)

        if sügavus > 1:
            pikkus /= 2
            suund = - suund
            ruutude_fraktal(sügavus - 1)
            suund = - suund
            pikkus *= 2

        right(suund)

    forward(pikkus)
    right(suund)

speed(0)
pikkus = 100
suund = 90
ruutude_fraktal(5)

exitonclick()
        
        
