from turtle import *
from random import *
speed(0)
def hulknurk(arv, pikkus):
    nurk= 180-(arv-2)*180/arv
    for el in range(arv):
        forward(pikkus)
        left(nurk)


for el in range(30):
    penup()
    goto(randint(-500,500),randint(-300,300))
    pendown()
    hulknurk(randint(3,20),randint(5,50))
    
    
exitonclick()