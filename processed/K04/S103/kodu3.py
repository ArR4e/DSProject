from turtle import *
from random import randint

def hulknurk(n, pikkus):
    nurk = ((n-2)*180)/n
    while n > 0:
        forward(pikkus)
        right(180-nurk)
        n -= 1
    

i = 0
while i < 30:
    hulknurk(randint(3,10), randint(20,100))
    i += 1
    penup()
    goto(randint(-300,0),randint(0,300))
    pendown()
exitonclick()