from turtle import Turtle, Screen, delay, speed, right, forward, backward, left, setx, sety, penup, pendown
from random import randint
def Hulknurk(pikkus, n):
    pööre = 360/n
    for i in range(n):
        forward(pikkus)
        right(pööre)

delay(0)
speed(-1)
for i in range(30):
    penup()
    setx(randint(-300, 300))
    sety(randint(-200, 200))
    pendown()
    Hulknurk(randint(20, 80), randint(3, 8))