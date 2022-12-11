from turtle import *
from random import *

speed(10)

def hulknurk(n,l):
    nurkade_summa=(n-2)*180
    nurk=nurkade_summa/n
    for i in range(n):
        forward(l)
        left(180-nurk)

for i in range(30):
    up()
    goto(randint(-300,300),randint(-300,300))
    down()
    hulknurk(randint(3,16),randint(0,50))
exitonclick() 
    