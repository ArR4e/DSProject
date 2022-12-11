from turtle import *
from random import randint
def hulknurk(n,pikkus):
    suurus=180-(n-2)*180/n
    for a in range(n):
        forward(pikkus)
        right(suurus)
for a in range(30):
    up()
    goto(randint(-500,500),randint(-500,500))
    down()
    hulknurk(randint(3,20),randint(50,100))