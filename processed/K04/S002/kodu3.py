from turtle import *
from random import randint

speed(0)
def hulknurk(n, x):
    for i in range(n):
        fd(x)
        left(360/n)

n = randint(3, 10)
for i in range(30):
    hulknurk(n, randint(50, 200)/n)
    penup()
    goto(randint(-300,300),randint(-300,300))
    pendown()
    n = randint(3, 10)

exitonclick()