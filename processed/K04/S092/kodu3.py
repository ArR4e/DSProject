from random import randint
from turtle import *

def hulknurk(n, a):
    nurk = 180 - (((n-2) * 180) / n)
    while n > 0:
        forward(a)
        right(nurk)
        n -= 1

for i in range(30):
    hideturtle()
    penup()
    goto(randint(-90, 90), randint(-90, 90))
    showturtle()
    pendown()
    hulknurk(randint(3, 20), randint(15, 100))