from random import*
from turtle import*

def külg(a,b):
    speed(10)
    forward(b)
    c=360/a
    left(c)
    left(90)

speed(10)
i=0
a=uniform(3,360)
b=uniform(10,250)


while i<=30:
    külg(a,b)
    i+=1 
exitonclick()