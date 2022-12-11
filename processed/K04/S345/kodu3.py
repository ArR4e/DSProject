from turtle import *
from random import randint

def f(kulgedearv, kuljepikkus):
    if kulgedearv == 3:
        nurk = 60
        while kulgedearv > 0:
            forward(kuljepikkus)
            left(120)
            kulgedearv -= 1
        exitonclick()
    else:
        nurk = 360//kulgedearv
        while kulgedearv > 0:
            forward(kuljepikkus)
            left(nurk)
            kulgedearv -= 1
        exitonclick()

n = 31
while True:
    edasi = randint(1, 100)
    poore = randint(0, 180)
    arv = randint(3, 10)
    pikkus = randint(1, 50)
    if n == 0:
        break
    else:
        f(5, 25)
        up()
        forward(edasi)
        right(poore)
        forward(edasi)
        down()
        n -= 1
        exitonclick()