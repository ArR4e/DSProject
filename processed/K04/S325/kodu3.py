from random import *
from turtle import *
def hn(n,l):
    i=1
    while n>=i:
        forward(l)
        right(360/n)
        i+=1
j=1
while j<=30:
    up()
    goto(randint(-200,200),randint(-150,150))
    setheading(randint(0,360))
    down()
    hn(randint(3,10),randint(10,100))
    j+=1

exitonclick()