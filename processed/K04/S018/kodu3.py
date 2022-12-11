from turtle import *
from random import randint

def hulknurk(n, l):
    nurk = 180 - (((n - 2)*180)/n)
    j = 0
    while j < 30:
        up()
        goto(randint(-500,500),randint(-500,500))
        down()
        i = 0
        while i < n:
            forward(l)
            right(nurk)
            i += 1
        j += 1
    exitonclick()

k_arv = int(input("Külgede arv: "))
k_pikkus = int(input("Külgede pikkus: "))
hulknurk(k_arv, k_pikkus)
    