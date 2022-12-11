from turtle import *
from random import randint
x=0
def hulknurk(a,p):
    for _ in range(a):
        forward(p)
        right(360/a)
#arv=int(input("sisesta nurkade arv: "))
#pikkus=int(input("sisesta küljepikkus: "))
#hulknurk(arv,pikkus)
while x<30:
    up()
    goto(randint(-100,100),randint(-100,100))
    arv=randint(3,25)
    pikkus=randint(10,100)
    down()
    hulknurk(arv,pikkus)
    x+=1
    
    
    