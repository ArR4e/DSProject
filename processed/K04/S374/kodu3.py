from random import randint
from turtle import *

def hulknurk (kulgede_arv, kuljepikkus):
    poore=360/kulgede_arv
    
    while kulgede_arv>0:
        forward(kuljepikkus)
        right(poore)
        kulgede_arv-=1
        
kuljed=int(input('Sisestage kulgede arv: '))
pikkus=float(input('Sisestage hulknurga uhe kulje pikkus: '))

for i in range (30):
    up()
    goto(randint(-400,400), randint(-400,400))
    down()
    hulknurk(kuljed, pikkus)
    
exitonclick()