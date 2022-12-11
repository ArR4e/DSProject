from turtle import *
from random import randint

def hulknurk(külgede_arv, küljepikkus):
    hulknurga_sisenurk = ((külgede_arv - 2) * 180) / külgede_arv
    külg = 0
    while külg < külgede_arv:
        forward(küljepikkus)
        left(180 - hulknurga_sisenurk)
        külg += 1

hulknurki = 0
while hulknurki < 30:
    hulknurk(randint(3, 10), randint(5, 20))
    up()
    forward(randint(10, 80))
    left(randint(1, 360))
    down()
    hulknurki += 1