from random import randint
from turtle import *

külgede_arv = 3
küljepikkus = 10
nurk = 180 - (külgede_arv - 2) * 180 / külgede_arv
def hulknurk(külgede_arv, küljepikkus):
    külgi_joonistatud = 0
    hulknurki = 0
    while hulknurki < 30:        
        while külgi_joonistatud  < külgede_arv:
            forward(küljepikkus)
            right(nurk)
            külgi_joonistatud += 1
        if külgi_joonistatud == külgede_arv:
            x = randint(1, 500)
            y = randint(1, 500)
            up()
            goto(x, y)
            down()
            külgi_joonistatud = külgi_joonistatud - külgede_arv
        hulknurki += 1
        if hulknurki == 30:
            break
hulknurk(külgede_arv, küljepikkus)
exitonclick()