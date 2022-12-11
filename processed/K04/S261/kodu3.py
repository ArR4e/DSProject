from turtle import *
import random

def hulknurk():
    n=random.randint(3,10)
    l=random.randint(50,500)
    x=180-(n-2)*180/n
    while n>0:
        n=n-1
        forward(l)
        right(x)
    up()
    left(random.randint(1,180))
    forward(random.randint(50,500))
    down()
i=1
while i<=30:
    hulknurk()