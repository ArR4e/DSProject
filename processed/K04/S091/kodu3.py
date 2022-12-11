from turtle import *
import turtle
from random import randint
import random

length = 600
height = 600
setup(length, height)
setworldcoordinates(0,0,length,height)

number = int(input("Sisesta soovitud külgede arv: "))
pikkus = int(input("Sisesta soovitud külje pikkus: "))

def hulknurk(number, pikkus):
    nurk = (180*(number-2))/number
    x = random.randint(0,500)
    y = random.randint(0,500)
    up()
    goto(x, y)
    down()
    for i in range(1, number+1):
        forward(pikkus)
        left(180-nurk)
        
for i in range(0,30):
    hulknurk(number, pikkus)
    


exitonclick()