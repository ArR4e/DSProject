import random
from turtle import *

i = 0

while i < 30:
    i += 1

    def hulknurk(külgede_arv, küljepikkus):
        joonistatud_kylgi = 0
        while joonistatud_kylgi < külgede_arv:
            forward(küljepikkus)
            left(nurk)
            joonistatud_kylgi += 1


    külgede_arv = random.randint(3, 6)
    küljepikkus = random.randint (30, 70)
    nurk = 360 / külgede_arv

    hulknurk(külgede_arv, küljepikkus)

    up()
    forward(random.randint(30,70))
    left(random.randint(10,100))
    forward(random.randint(30,70))
    down()





