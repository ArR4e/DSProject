import random
from turtle import *
a=random.random()*500
b=random.random()*500
t=360/b


def nurk(a,b):
    while b!=0:
        fd(a)
        lt(t)
        b-=1
x=30    
while x >= 0:
    nurk(a,b)
    up()
    goto(random.random()*500,random.random()*500)
    down()
    x-=1
    
