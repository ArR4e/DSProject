from random import randint
from turtle import *

def hulknurk(kyljed, pikkus):
    a = 180-(180*(kyljed-2))/kyljed
    for x in range(kyljed):
        fd(pikkus)
        rt(a)
    
    
nr1 = int(input("Külgede arv: "))
nr2 = int(input("Külgede küljepikkus: "))

i=0
while i < 30:
    up()
    goto(randint(-300,300),randint(-300,300))
    down()
    hulknurk(nr1,nr2)
    i = i + 1
    
done()