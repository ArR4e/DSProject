from turtle import *
speed(0)
def f(a, l):
    i = 0
    while i < a:
        forward(l)
        right(((a-(a-2))*180)/a)
        i += 1
from random import randint
i = 0
while i < 30:
    up()
    forward(randint(50,85))
    down()
    left(randint(30,90))
    f(randint(3,21), randint(50,100))
    i += 1

exitonclick()