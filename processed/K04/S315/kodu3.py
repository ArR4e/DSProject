from turtle import *
from random import *

def kilp(a, k):

    for i in range(0,a):

        n = ((180*(a-2))/a)
        forward(k)
        right(180- n)
    exitonclick()
    

for i in range(0,30):

    a = randint(2, 100)
    k = randint(1, 100)
    kilp(a,k)
    p = randint(1, 100)
    setpos(p,p)
    