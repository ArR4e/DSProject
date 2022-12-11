from turtle import *
from random import randint

#kyljed =  int(input("Sisesta külgede arv: "))
#pikkus =  int(input("Sisesta küljepikkus: "))
kyljed = randint(4,30)
pikkus = randint(10, 100)
nurk = (360 / kyljed)
a = 0
def hulknurk(kyljed, pikkus):
    m = 0
    nurk = (360 / kyljed)
    speed(100)
    while m < kyljed:
        forward(pikkus)
        left(nurk)
        m += 1
while a < 30:
    
    up()
    setx(randint(-200,200))
    sety(randint(-200,200))
    down()
    a += 1
        
    kyljed = randint(4,20)
    pikkus = randint(10, 100)
        
     
    hulknurk(kyljed, pikkus)
exitonclick()