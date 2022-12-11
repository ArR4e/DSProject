from turtle import *
import random

def hulknurk(arv, pikkus):
    nurk = ((arv-2)*180)/arv+180
    for x in range(arv):
        fd(pikkus)
        lt(nurk)
speed(-1)
for x in range(30):
    penup()
    goto(random.randint(-500,500),random.randint(-500,500))
    pendown()
    hulknurk(random.randint(3,10),random.randint(10,100))