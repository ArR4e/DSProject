from turtle import *
from random import randint

def hulknurk(r, x):
    külgi = 0
    while külgi < r:
        forward(x)
        left(360/r)
        külgi += 1

def uuskoht():
    up()
    forward(randint(0, 200))
    left(randint(0, 200))
    forward(randint(0, 200))
    down()

i = 0
while i < 30:
    r = randint(3, 24)
    x = randint(0, 100)
    hulknurk(r, x)
    uuskoht()

exitonclick()