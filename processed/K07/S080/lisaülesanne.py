from turtle import *
from random import (randint)
import secrets
a = 200
pensize(3)
b = 1
#speed(10)
c = []
n = 2000
for i in range(n):
    c.append('#%06X' % randint(0,0xFFFFFF))
speed(500)
while b <= 360: #c != []:
    suva = secrets.choice(c)
    värv = color(suva)
    c.remove(suva)
    fd(a)
    bk (a)
    rt(181)
    b = b + 1
exitonclick()
