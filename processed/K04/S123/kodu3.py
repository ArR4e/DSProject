from turtle import*
from random import randint

def hnurk(arv, pikkus):
    sisenurkade_summa=(arv-2)*180
    nurga_suurus=sisenurkade_summa/arv
    i=0
    while i < arv:
        forward(pikkus)
        left(180-nurga_suurus)
        i += 1
        
j=0
while j<=30:
    hnurk(randint(3,10), randint(10,50))
    j += 1
    up()
    forward(randint(11, 200))
    left(randint(1, 360))
    forward(randint(11, 200))
    down()

exitonclick()