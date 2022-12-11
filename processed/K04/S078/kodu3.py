from turtle import *
from random import randint

x=0
def hulknurk(n, a):
    i=0
    while i<n:
        forward(a)
        left(360/n)
        i += 1
        
while x<30:
    k_arv = randint(3, 15)
    pikkus = randint(50, 250)
    hulknurk(k_arv, pikkus)
    up()
    left(randint(0, 359))
    forward(randint(20, 300))
    down()
    x += 1

    
exitonclick()