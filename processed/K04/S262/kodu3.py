from turtle import *
from random import *
def joonistaja(x,y):
    z = 360/x
    t = 0
    forward(y)
    while t < x:
        right(z)
        forward(y)
        t += 1

i = 0
while i < 30:
    penup()
    right(randint(0,360))
    forward(randint(1,500))
    pendown()
    joonistaja(randint(1,20),randint(1,5))
    i += 1