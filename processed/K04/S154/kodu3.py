from math import *
from turtle import *
import random

a = random.randint(3, 10)
b = random.randint(10, 100)
e = random.randint(200, 300)
v = random.randint(50, 180)
kraad = 0

def hulknurk(arv, pikkus):
    i = 0
    kraad = 180 - (((arv - 2) * 180)/ arv)
    while i < arv:
        forward(pikkus)
        left(kraad)
        i = i + 1
print(hulknurk(8, 50))

def suva(edasi, vasak):
    forward(edasi)
    left(vasak)

k = 0
while k < 10:
    penup()
    print(suva(e, v))
    pendown()
    print(hulknurk(a, b))
    k = k + 1





exitonclick()