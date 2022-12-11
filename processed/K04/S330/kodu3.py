from turtle import *
from random import *

n = 0
a = 0

def hulknurk(n, a):
    hulknurki = 1
    while hulknurki < 30:
        n = randint(3, 10)
        a = randint(1, 150)
        x = (randint(-400, 0), randint(0, 400))
        up()
        setpos(x)
        down()
        hulknurki += 1
        nurki = 0
        while nurki < n:
            forward(a)
            right(180-(180*(n-2))/n)
            nurki += 1
hulknurk(n, a)
exitonclick()
    