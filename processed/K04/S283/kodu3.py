from turtle import *
import random

def hulknurgad(küljed, pikkus):
    küljed2 = küljed
    while küljed > 0:
        forward(pikkus)
        right(360/küljed2)
        küljed -= 1
    up()
    left(random.randint(90, 180))
    forward(random.randint(90,180))
    down()

speed(10)
delay(0)
i = 0
while i < 30:
    küljed = random.randint(0, 10)
    pikkus = random.randint(10, 50)
    hulknurgad(küljed, pikkus)

exitonclick()