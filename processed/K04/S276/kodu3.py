import random
from random import randint
from turtle import *
n=0
while n < 30:
    penup()
    goto(randint(-300,300),randint(-300,300))
    pendown()
    n=n+1
    m=0
    külgi=random.randint(3,10)
    pikkus=random.randint(10,60)
    while m < külgi:
        forward(pikkus)
        left(180-180*(külgi-2)/külgi)
        m=m+1