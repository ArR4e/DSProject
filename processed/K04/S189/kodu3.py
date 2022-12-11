from turtle import *
from random import randint

speed(50)

def hulknurk(arv, pikkus):
    i=0
    kraad=360/arv
    while (i<arv):
        forward(pikkus)
        left(kraad)
        i+=1
        
j=0
while (j<30):
    hulknurk(randint(3,10), randint(20,100))
    up()
    hideturtle()
    forward(randint(25,100))
    right(randint(1,90))
    showturtle()
    down()
    j+=1


exitonclick()
        
        
    

