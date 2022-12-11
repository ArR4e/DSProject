from turtle import*
from random import randint

def kuju(n,k):
    nurk = 360/n
    while n>0:
        fd(k)
        right(nurk)
        n=n-1
i=0
while i<30:
    penup()
    goto(randint(-500,500),randint(-500,500))
    pendown()
    kuju(randint(10,15),randint(18,180))
    i=i+1
    
exitonclick()