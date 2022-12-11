from turtle import *
from random import randint

def hulknurk(a, n):
    i=0
    while i < n:
        forward(a)
        left(360/n)
        i+=1
    
for x in range(30):
    down()
    begin_fill()
    hulknurk(randint(10,30),randint(3,5))
    end_fill()
    up()
    forward(randint(50,150))
    left(randint(60,120))
    forward(randint(50,150))
    

exitonclick()