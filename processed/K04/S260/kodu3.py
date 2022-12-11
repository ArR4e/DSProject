from turtle import *
from random import *
speed(0)

def hulknurk(n,s):
    for i in range(n):
        forward(s)
        left(360/n)

for i in range(30):
    penup()
    goto(randint(-800,800),randint(-800,800))
    pendown()
    hulknurk(randint(3,15),randint(10,150))