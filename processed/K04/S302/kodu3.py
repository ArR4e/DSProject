from turtle import *
from random import randint

def joonis(kyljed, pikkus):
    nurk = 180 - ((180 * (kyljed -2)) / kyljed)
    while kyljed > 0:
        down()
        forward(pikkus)
        left(nurk)
        kyljed -= 1
        up()

a = 30
up()
while a > 0:
    kyljed = randint(1,30)
    pikkus = randint(1,200)
    joonis(kyljed, pikkus)
    poore = left(45)
    edasi = forward(100)
    a -=1
excitonclick()