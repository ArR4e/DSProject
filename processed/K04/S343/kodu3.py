from turtle import *
import random



def kilbu():
    i=1
    up()   
    setpos(random.randint(0, 300), random.randint(0, 300))
    down()
    a=random.randint(3,15)
    b=random.randint(10, 60)
    while i <= a:
        nurk = ((a-2)*180)/a
        forward(b)
        right(180-nurk)
        i = i + 1
n=0
while n<=30:
    kilbu()
    n = n+1
exitonclick()