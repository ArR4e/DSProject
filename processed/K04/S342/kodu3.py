from turtle import *
import random
arv = random.randint(3, 10)
pikkus = random.randint(20, 70)
x = random.randint(-300, 300)
y = random.randint(-300, 300)


def hulknurk(arv, pikkus):
    kordus = 0
    while kordus < arv:
        forward(pikkus)
        right(360/arv)
        kordus += 1

hulknurgad = 0
while hulknurgad < 30:
    up()
    goto(x, y)
    down()
    hulknurgad += 1
    hulknurk(arv, pikkus)
    arv = random.randint(3, 10)
    pikkus = random.randint(20, 70)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

exitonclick()