from turtle import *
from random import randint

import turtle
kylg = 5
pikkus = 20

def juhuslik():
    a = randint(20, 50)
    b = randint(20, 100)
    c = randint(0, 360)
    penup()
    fd(a)
    rt(c)
    fd(b)
    pendown()

def hulknurk(a, b):
    nurk = 360/a
    i = 0
    while i < a:
        fd(b)
        rt(nurk)
        i += 1
i = 0
while i < 30:
    hulknurk(kylg, pikkus)
    juhuslik()

exitonclick()
