import random
from turtle import *

def kylik(arv, pikkus):
    joonistatud_kylgi = 0
    while joonistatud_kylgi < arv:
        forward(pikkus)
        left(360/arv)
        joonistatud_kylgi += 1

kylikuid = 0
while kylikuid < 30:
    arv = random.randint(3,11)
    pikkus = random.randint(22,222)
    kylik(arv, pikkus)
    a=random.randint(80,100)
    b=random.randint(45,360)
    c=random.randint(80,100)
    up()
    forward(a)
    left(b)
    forward(c)
    down()
    kylikuid += 1