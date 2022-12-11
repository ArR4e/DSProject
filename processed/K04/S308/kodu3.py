from turtle import *
from random import randint

def hulknurk(kylg):
    i = 0
    while i < kylg:
        forward(b)#ei tea veel oleneb hulknurgas
        left(360//kylg)
        i += 1
def kuhu():
    up()
    goto(randint(-500,500),randint(-500,500))
    down()
i=0
b=0
while i <=30:
    b=randint(-100,200)
    hulknurk(randint(3,10))
    kuhu()
    i+=1

exitonclick()