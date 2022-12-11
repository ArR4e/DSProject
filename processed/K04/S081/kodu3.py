from turtle import *
from random import randint
def f(k, p):
    speed(1000)
    n = 180-((180*(k-2))/k)
    a=0
    x= randint(-300, 300)
    y= randint(-300, 300)
    up()
    goto(x,y)
    down()
    while a < k:
        fd(p)
        lt(n)
        a+=1
        

c = 0

while c < 30:
    k = randint(3,12)
    p = randint(20, 70)
    f(k,p)
    c+=1

exitonclick()


