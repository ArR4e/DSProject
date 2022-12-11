from math import sin, pi
from turtle import*
from random2 import*
#setpos(460,370)
speed(0)
def hulknurk(n, l):
    up()
    forward(l/2/sin(pi/n))
    left(90)
    down()
    forward(l/2)
    a=0
    for a in range(n-1):
        left(360/n)
        forward(l)
    left(360/n)
    forward(l/2)
n=int(input("Palun sisestage hulknurda nurkade arv: "))
l=float(input("Palun sisestage huknurga kuljepikkus: "))
b=0
for b in range(30):
    x=randint(-450,450)
    y=randint(-350,350)
    up()
    setpos(x,y)
    down
    hulknurk(n, l)
exitonclick()