from turtle import *
from random import randint


def hulknurk(kulg,pikkus):
    for i in range(30):
        penup()
        goto(randint(-100,0),randint(0,100))
        pendown()
        for i in range(kulg):
            forward(pikkus)
            left(180-(((kulg-2)*180)/kulg))

hulknurk(10,100)