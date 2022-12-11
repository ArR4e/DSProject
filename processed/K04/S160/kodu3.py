from turtle import *
import random

def hulknurk(n):
    i = 0
    nurga_arvutus = 360 / n
    while (i < n):
        forward(m)
        left(nurga_arvutus)
        i = i + 1

n = random.randint(3, 30+1)
m = random.randint(10, 150)

hulknurk(n)

exitonclick()
    