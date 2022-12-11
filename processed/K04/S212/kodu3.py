from random import randint
from turtle import forward, left, exitonclick, setpos, up, down

def hulknurk(n,x):
    i = n
    angle = 180-180*(n-2)/n
    while i>0:
        forward(x)
        left(angle)
        i -= 1

i = 30
while i > 0:
    up()
    setpos(randint(-500,500),randint(-400,400))
    down()
    hulknurk(randint(3,10),randint(10,90))
    
    i -= 1
exitonclick()