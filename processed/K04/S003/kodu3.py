from turtle import *
from random import randint
def hulknurk(n,l):
    nurk = 360/n
    while n > 0:
        fd(l)
        right(nurk)
        n -= 1

i = 0
while i < 30:
    penup()
    goto(randint(-200,200),randint(-200,200))
    pendown()
    hulknurk(randint(3,15),randint(10,100))
    i +=1


exitonclick()