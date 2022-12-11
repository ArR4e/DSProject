from turtle import *
from random import *

def hulknurk(külgi, pikkus):
    joonistatud_kylgi = 0
    nurk = 360/külgi
    while külgi > 0:
        forward(pikkus)
        left(nurk)
        külgi -= 1
def koht():
    up()
    forward(randint(1,360))
    left(randint(1,360))
    forward(randint(1,360))
    down()

x = 0
while x < 30:        
    külgi = randint(3,20)
    pikkus = randint(10, 200)
    hulknurk(külgi, pikkus)
    koht()
    x += 1

