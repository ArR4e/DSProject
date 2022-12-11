from turtle import *
from random import randint

def hulknurk(külgi, a):
    joonistatud_kylgi = 0
    while joonistatud_kylgi <= külgi:
        pööra = 360/külgi
        right(pööra)
        forward(a)
        joonistatud_kylgi += 1

külgi = float(input('Külgede arv: '))
a = float(input('Küljepikkus: '))

i=0
while i<30:
    hulknurk(külgi,a)


    up()
    forward(randint(1,150))
    left(randint(1,360))
    forward(randint(1,150))
    down()
    
    i +=1

exitonclick()