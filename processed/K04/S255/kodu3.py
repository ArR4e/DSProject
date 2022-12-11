from turtle import *
from random import randint
screensize(4000, 4000)
# arv_kulg = int(input('Sisesta külgede arv: '))
# pikkus_kulg = int(input('Sisesta külje pikkus: '))
speed(0)
def hulknurk(arv_kulg, pikkus_kulg):
    for i in range(arv_kulg):
        forward(pikkus_kulg)
        right(360/arv_kulg)
for i in range(30):
    penup()
    setpos(randint(-500, 500), randint(-500, 500))
    pendown()
    arv_kulg = randint(3, 50)
    pikkus_kulg = randint(1, 200)
    hulknurk(arv_kulg, pikkus_kulg)
    
exitonclick()