import turtle
import random
from random import randint

def hulknurk(n, l):
    joonistatud_külgi=0
    while joonistatud_külgi<=n:
        forward(l)
        left(360/n)
        joonistatud_külgi += 1
n=randint(0, 10)
l=randint(0, 100)

def liikumine(x, y, z):
    up()
    forward(x)
    left(y)
    forward(z)
    down()
x=randint(0, 100)
y=randint(0, 360)
z=randint(0, 100)

hulknurkade_arv=0
while hulknurkade_arv <=30:
    hulknurk(n, l)
    liikumine(x, y, z)
    
exitonclick()