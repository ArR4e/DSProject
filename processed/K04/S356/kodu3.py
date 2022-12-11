from turtle import *
from random import randint

def hulknurk(arv,pikkus):
    i = 0
    while i < 30:
        hulk(arv,pikkus)
        koht()
        i += 1
        
def hulk(arv,pikkus):
    arv = randint(3,10)
    pikkus = randint(10,50)
    nurk = 360 / arv
    i = 1
    while i <= arv:
        forward(pikkus)
        left(nurk)
        i += 1
        
def koht():
    up()
    goto(randint(-500,500),randint(-500,500))
    down()

speed(0)
arv = randint(3,10)
pikkus = randint(10,50)
hulknurk(arv,pikkus)
exitonclick()