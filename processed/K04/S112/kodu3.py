from turtle import *

from random import randint

arv = randint(3,10)
pikkus = randint(10,200)

speed(10)

def kilpkonn(arv,pikkus):
    joonistatud_külgi = 0
    while joonistatud_külgi < arv:
        forward(pikkus)
        left(360/arv)
        joonistatud_külgi += 1
        
def liikumine():        
    up()
    left(randint(90,360))
    forward(randint(10,100))
    down()

hulknurgad = 0
while hulknurgad < 30:
    kilpkonn(randint(3,10),randint(10,200))
    liikumine()
    hulknurgad += 1



    


