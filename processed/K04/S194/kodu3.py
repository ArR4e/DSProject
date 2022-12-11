from turtle import *
from random import randint

def hulknurk(n, a):
    x = 0
    while x< n:
        forward(a)
        left(360/n)
        x += 1

y  = 0
while y <= 30:
    hulknurk(randint(3, 10), randint(10, 34))
    up()
    left(randint(0, 360))
    forward(randint(30, 100))
    down()
    y += 1

