from turtle import *
from random import randrange

speed(10)
delay(0)

def hulknurk(n, külg):
    for i in range(n):
        forward(külg)
        right(360/n)

for x in range(0, 31):
    hulknurk(randrange(3, 8), randrange(20, 50))
    up()
    left(randrange(100, 200))
    forward(randrange(250, 300))
    down()

exitonclick()