from turtle import *
from random import randint

def hulknurk(a, b):
    nurk = 360 / a
    
    down()
    for i in range(a):
        forward(b)
        left(nurk)
    
    up()
    right(randint(0, 45))
    forward(randint(30, 50))
    
for i in range(30):
    a = randint(3, 8)
    b = randint(10, 40)
    hulknurk(a, b)
    
exitonclick()
