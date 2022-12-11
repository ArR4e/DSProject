from turtle import*
from random import*

def ruut(a,b):
    penup()
    goto(randint(-500,0), randint(0,500))
    pendown()
    while a > 0:
        forward(b)
        right(c)
        a -= 1
        

i = 0
while i < 30:
    a = randint(3,10)
    b = randint(10,30)
    c = 360/a
    ruut(a,b)
    i += 1
exitonclick()