from turtle import*
from random import randint
speed(0)
külgede_arv=randint(3, 40)
küljepikkus=randint(10, 150)
j=0
suvaline_nurk=randint(0, 360)
suvaline_distants=randint(0, 500)
kordaja=randint(0, 1)
def hulknurk(külgede_arv, küljepikkus):
    i=0
    while i < külgede_arv:
        fd(küljepikkus)
        right(180+(külgede_arv - 2) * 180 / külgede_arv)
        i+=1

while j < 30:
    külgede_arv=randint(3, 40)
    küljepikkus=randint(10, 150)
    hulknurk(külgede_arv, küljepikkus)
    up()
    if kordaja == 1:
        left(suvaline_nurk +180)
    else:
        right(suvaline_nurk + 180)
    fd(suvaline_distants)
    down()
    j+=1