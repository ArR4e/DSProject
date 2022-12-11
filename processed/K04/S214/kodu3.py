from turtle import*
from random import randint

def hulknurk(arv,mõõt):
    nurk = 180-((arv-2)*180)/arv
    while arv>=1:
        forward(mõõt)
        right(nurk)
        arv-=1

i=30
while i>=1:
    a = randint(10,100)
    b = randint(3, 12)
    hulknurk(b,a)
    x = randint(-300,300)
    y = randint(-300,300)
    penup()
    goto(x,y)
    pendown()
    i-=1
exitonclick()