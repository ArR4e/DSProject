from turtle import *
from random import randint

setworldcoordinates(0, 1000, 1000, 0)

def joonista(kylg, pikkus):
    for i in range(kylg):
        forward(pikkus)
        right(360/kylg)



for i in range(30):
    a = randint(3, 15)
    b = randint(15, 75)
    up()
    goto(randint(b, 1000-b), randint(b, 1000-b))
    down()
    joonista(a, b)

exitonclick()