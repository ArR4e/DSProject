from turtle import *
from random import random, choice, randint
def f(n,m):
    for i in range(n):
        forward(m)
        left(180-((n-2)*180)/n)
ht()
speed(10)
delay(0)
for i in range(30):
    pu()
    goto(choice([-1,1])*500*random(),choice([-1,1])*500*random())
    pd()
    f(randint(3,20),random()*100)
    