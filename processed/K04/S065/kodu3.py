# 3. Hulknurgad

from turtle import *
from random import randint

def hulknurk(nurki, külgi):
    i = 0
    while i < nurki:
        i = i + 1
        fd(külgi)
        right(360/nurki)
        
a = 0
while a < 30:
    a = a + 1
    penup()
    goto(randint(-300,250),randint(-300,250))
    pendown()
    hulknurk(randint(3,20),randint(10,60))