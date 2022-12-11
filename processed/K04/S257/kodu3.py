from turtle import *
from random import randint
def hulknurk(k_arv, k_pikkus):
    k_nurk = (k_arv-2)*180/k_arv
    for i in range(k_arv):
        fd(k_pikkus)
        lt(180-k_nurk)
speed(10)
for i in range(30):
    pu()
    goto(randint(-200, 200), randint(-200,200))
    pd()
    hulknurk(randint(3, 10), randint(10,50))
exitonclick()