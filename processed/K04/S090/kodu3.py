from turtle import *
from random import randint

def hulknurk(a, b):
    kuljed = 0
    while kuljed < a:
        forward(b)
        left(360/a)
        kuljed += 1

i = 0
while i < 30:
    x = randint(3, 10)
    y = randint(1, 30)
    z = randint(0, 100)
    j = randint(0, 100)
    hulknurk(x, y)
    penup()
    forward(z)
    left(j)
    pendown()
    
    