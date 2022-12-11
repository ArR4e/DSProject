from turtle import *
from random import randint
def hulknurk(ka, kp):
    joonistatud = 0
    while joonistatud < ka:
        forward(kp)
        right(nurk)
        joonistatud += 1
def liigu():
    up()
    forward(randint(25, 75))
    left(randint(25, 165))
    forward(randint(50, 150))
    down()
a = 0
while a < 30:
    ka = randint(3, 10)
    kp = randint(25, 175)
    nurk = 360 / ka
    hulknurk(ka, kp)
    liigu()
    a += 1

