from turtle import *

pikkus = 100
kraad = 90

speed(0)

def joonis(arv):
    global pikkus, kraad

    for i in range(3):
        forward(pikkus)
        if arv > 1:
            pikkus /= 2
            kraad = - kraad
            joonis(arv-1)
            pikkus *= 2
            kraad = - kraad
            
        right(kraad)
    forward(pikkus)
    right(kraad)
        


joonis(4)
exitonclick()
