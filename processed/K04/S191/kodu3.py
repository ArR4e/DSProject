from turtle import *
from random import randint

m=0
n=0
setworldcoordinates(-500,-500,500,500)

def kujund(m,n):
    i=30
    a=0
    while i>0:
        a=0
        n=randint(3,16)
        m=randint(5,30)
        x=randint(-500,450)
        y=randint(-450,500)
        up()
        goto(x,y)
        down()
        p=(360/n)
        while a<n:
            forward(m)
            right(p)
            a+=1
        i-=1
kujund(m,n)
exitonclick()




