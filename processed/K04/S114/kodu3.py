from turtle import *

def pilt(a,kuljepikkus):
    tehtud_jooned = 0
    
    while tehtud_jooned < a:
        b = (360/a)
        left(b)
        forward(kuljepikkus)

        tehtud_jooned += 1
pilt(3,55)
exitonclick()