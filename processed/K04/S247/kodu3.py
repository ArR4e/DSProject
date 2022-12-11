from turtle import *
from random import randint
def hulknurk(n,l):
    nurk=360/n
    while n > 0:
        fd(l)
        right(nurk)
        n-=1
i=0
while i<30:
    penup()
    goto(randint(-200,200),randint(-100,100))
    pendown()
    hulknurk(randint(2,14),randint(15,150))
    i+=1

exitonclick()