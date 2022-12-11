from turtle import *
import random

def f(külgi,pikkus):
        return (forward(pikkus), right(sisenurk))




i = 0
while i <= 30:
    külgi = random.randint(3, 10)
    pikkus = random.randint(10, 100)
    sisenurk = float((180 - ((külgi - 2) * 180) / külgi))
    while külgi > 0:
    
        f(külgi,pikkus)
        külgi -= 1
    up()
    right(random.randint(0,360))
    forward(random.randint(100,250))
    down()
    i += 1

exitonclick()
    