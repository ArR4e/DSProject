from turtle import *

def ruudud(s):
    global pikkus, kraad
    
    for _ in range(3):
        forward(pikkus)
        
        
        if s > 1:
            pikkus/= 2
            kraad = - kraad
            ruudud(s-1)
            kraad = - kraad
            pikkus *= 2


        right(kraad)


    forward(pikkus)
    right(kraad)


pikkus = 100
kraad = 90


ruudud(4)

hideturtle()
exitonclick()