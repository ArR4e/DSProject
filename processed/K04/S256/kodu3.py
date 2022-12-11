from turtle import *
import random


def go (hulk, pikkus):
    sisenurk = 360 / hulk
    külgnurk = (180 - sisenurk) / 2
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    up()
    setposition(x, y)
    right(90)
    down()
    i = 0
    while i <hulk:
        forward(pikkus)
        right(180 - (2 * külgnurk))
        i += 1
    up()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    setposition(x, y)
    down()
    

hulk = int(input("mitu külge hulknurgal on?: "))
pikkus = int(input("mis on külje pikkus?: "))

s=0
while s < 30:
    go(hulk,pikkus)
    s += 1
exitonclick()