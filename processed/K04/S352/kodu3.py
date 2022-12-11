from turtle import*
from random import randint

def nurk(n):
    return ((n-2)*180)/n
speed(9)
for i in range(30):
    x=randint(-400,400)
    y=randint(-200,400)
    
    n=randint(3,8)
    l=randint(5,200)
    
    pu()
    setpos(x,y)
    pd()
    for j in range(n):
        fd(l)
        rt(180-nurk(n))
exitonclick()