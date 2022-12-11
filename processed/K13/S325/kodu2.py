from turtle import *

def fraktal(l,r):
    for i in range(3):
        forward(l)
        if r>1:
            fraktal(l/2,r-1)
        if r%2==0:
            right(90)
        else:
            left(90)
    forward(l)
    if r%2==0:
        right(90)
    else:
        left(90)
    
    

up()
goto(-50,0)
speed(0)
down()
fraktal(80,7)
exitonclick()