from turtle import *
from random import randint
def f(küljed, pikkus):
    i = küljed
    while küljed >= 0:
        forward(pikkus)
        right(360 / (i))
        küljed -= 1

i = 0
while i < 30:
    f(randint(3,8), randint(10,150))
    i += 1
    penup()
    goto(randint(-400,0), randint(0,400))
    pendown()
exitonclick()