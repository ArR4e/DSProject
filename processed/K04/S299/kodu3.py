from random import*
from turtle import*

def hulknurk(kylgi, kyljepikkus):
    while kylgi>0:
        forward(float(kyljepikkus))
        left(360/kylgi)
        kylgi-=1
    
kylgi=randint(0,360)
kyljepikkus=int(random()*100)

joonistatud_kujundeid=0
while joonistatud_kujundeid <30:
    hulknurk(kylgi, kyljepikkus)
    up()
    forward(int(random()*100))
    left(randint(0,360))
    forward(int(random()*100))
    down()
    joonistatud_kujundeid +=1
    
exitonclick()