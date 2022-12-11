from turtle import*
from random import randint

def hulknurk(külg, pikkus):
    i=0
    n=float(külg)
    while i<n:
        forward(pikkus)
        right(180-(180*n-360)/n)
        i+=1
def liikumine():
    up()
    forward(randint(30,50))
    right(randint(0,360))
    forward(randint(30,50))
    down()

i=0
while i<30:
    külg=randint(3,10)
    pikkus=randint(10,50)
    hulknurk(külg,pikkus)
    liikumine()
    i+=1
