from turtle import*
from random import randint, randrange

def hulknurk(küljed, küljepikkus):
    
    nurk = ((180*(küljed-2)/küljed))
    i = 0
    while i < küljed:
        
        forward(küljepikkus)
        left(180-nurk)
        i = i+1
    
tehtud = 0
while tehtud < 30:
    küljed = randint(3, 50)

    küljepikkus = randint(5, 50)
    penup()
    goto(randint(-200,200), randint(-200,200))
    pendown()
    hulknurk(küljed, küljepikkus)
        
    tehtud = tehtud + 1

    

exitonclick()
    
    