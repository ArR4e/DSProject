from turtle import*
from random import randint

külgede_arv=randint(3,20)
küljepikkus=randint(1,100)
a=((külgede_arv-2)*180)/külgede_arv #Hulknurga sisenurk

def hulknurk(külgede_arv,küljepikkus):
    i=0
    while i<külgede_arv:
        forward(küljepikkus)
        right(180-a)
        i+=1

j=0
speed(30)
pencolor("green")
while j<=30:
    hulknurk(külgede_arv,küljepikkus)
    up()
    forward(randint(0,300))
    left(randint(0,360))
    down()
    j+=1


exitonclick()    