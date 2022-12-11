#hulknurgad

from turtle import *
from math import radians, sin
from random import randint

def hulknurk(n, küljepikkus):
    alfa = int(360/int(n))    
    i = 0
    while i<=n:
        forward(küljepikkus)
        right(alfa)
        i = i + 1
    
o=0
while o<=30:
    n=randint(1,30)
    küljepikkus=randint(1,300)
    hulknurk(n, küljepikkus)
    up()
    left(randint(1,360))
    forward(randint(1, 25))
    down()
    o = o + 1
