from turtle import *
from random import *
def joonista():
    arv = randint(3,10)
    arv2 = arv
    pikkus = randint(1,100)
    while arv2 > 0:
        forward(pikkus)
        right(180-(arv-2)*180/arv)
        arv2 -= 1

i = 0
while i < 30:
    i += 1
    down()
    joonista()
    up()
    goto(randint(-300,300),randint(-300,300))
    
exitonclick()
