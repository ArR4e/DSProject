from turtle import *
import random

speed(0)
def hulknurk(kylgi, pikkus):
    i = 0
    nurk=360/kylgi
    down()
    while i < kylgi:
        forward(pikkus)
        left(nurk)
        i = i + 1
    up()
    
def suvalised():
    left(random.randint(1, 360))
    forward(random.randint(30, 70))
    right(random.randint(1, 360))
    forward(random.randint(30, 70))

i = 0
while i < 30:
    hulknurk(random.randint(3, 10), random.randint(10, 50))
    suvalised()
    i = i + 1

exitonclick()