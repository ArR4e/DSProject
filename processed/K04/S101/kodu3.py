from turtle import *
from random import randint

n=int(input("sisesta hulknurga külgede arv:"))
l=float(input("sisesta küljepikkus:"))
speed(0)

def hulknurk(x,y):
    for i in range(x):
        forward(y)
        left(180-(x-2)*180/x)
def suvaline_hulknurk():
    for i in range(5000):
        a=randint(3,15)
        b=randint(15,100)
        up()
        goto(randint(-350,350),randint(-350,350))
        down()
        for s in range(a):
            
            forward(b)
            left(180-(a-2)*180/a)
            
hulknurk(n,l)
suvaline_hulknurk()

exitonclick()
    
