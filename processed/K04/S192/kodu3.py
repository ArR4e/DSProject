from turtle import *
from random import randint
def korraparane_hulknurk(kylgede_arv, kylje_pikkus):
    joonistatud_kylgi = 0
    nurk = 360/kylgede_arv
    while joonistatud_kylgi < kylgede_arv:
        forward(kylje_pikkus)
        left(nurk)
        joonistatud_kylgi += 1
joonistatud = 0
while joonistatud < 30:
    korraparane_hulknurk(randint(3,20), randint(10,25))
    up()
    left(randint(0,360))
    forward(randint(0,100))
    down()
    joonistatud += 1
exitonclick()