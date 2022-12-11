from turtle import *

def ruutude_fraktal(sügavus):
    if sügavus == 0:
        return
    global laius, suund
    for i in range(3):
        forward(laius)
        if sügavus > 1:
            laius = laius/2
            suund = -suund
            ruutude_fraktal(sügavus-1)
            suund = -suund
            laius *= 2
        right(suund)
    forward(laius)
    right(suund)

laius = 100
suund = 90
ruutude_fraktal(5)
exitonclick()
  