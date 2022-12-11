from turtle import *
from random import randint
colormode(255)
speed(10)
def hulknurk(külg, pikkus):
    külgede_arv = külg
    fillcolor(randint(0,255),randint(0,255),randint(0,255))
    begin_fill()
    for i in range(külgede_arv):
        forward(pikkus)
        right(360/külg)
    end_fill()
for i in range(30):
    hulknurk(randint(3,12), randint(20,100))
    penup()
    setpos(randint(-300,300),randint(-300,300))
    pendown()