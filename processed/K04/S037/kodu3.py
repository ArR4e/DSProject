from turtle import *
from random import randint

def hulknurk():
    i = 0
    nurk = float(180 - ((külgi - 2) * 180) / külgi)
    while i < külgi :
        forward(pikkus)
        left(nurk)
        i += 1
        
külgi = randint(3, 15)
pikkus = randint(10, 80)
arv = 30

while arv > 0:
    hulknurk()
    arv -= 1
    penup()
    forward(randint(10, 50))
    up()
    forward(randint(10, 50))
    left(randint(1, 360))
    down()
    pendown()
    

exitonclick()