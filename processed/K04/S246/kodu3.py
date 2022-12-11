from turtle import *
from random import randint

def hulknurk(kylgede_arv, kyljepikkus):
    kylgede_arv = randint(3, 30)
    kyljepikkus = randint(1, 200)
    nurga_suurus = 180 - ((180 * (kylgede_arv - 2)) / kylgede_arv)
    while kylgede_arv > 0:
        down()
        forward(kyljepikkus)
        left(nurga_suurus)
        kylgede_arv -= 1
        up()
def tsykkel(pööre, edasi):
    hulknurk(kylgede_arv, kyljepikkus)
    pööre = left(45)
    edasi = forward(140)

kylgede_arv = randint(1, 30)
kyljepikkus = randint(1, 200)
up()
pööre = left(45)
edasi = forward(140)
kordus = 30
while kordus > 0:
    tsykkel(pööre, edasi)
    kordus -= 1

exitonclick()