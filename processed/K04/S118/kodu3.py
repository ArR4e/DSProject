from turtle import *
import random as rn
speed(10)
delay(0)

def hulknurk(külg_arv, pikkus):
    pöördenurk = ((külg_arv-2)*180)/külg_arv-180
    for i in range(0, külg_arv):
        fd(pikkus)
        right(pöördenurk)
        
for i in range(0,30):
    x = rn.randint(-300,300)
    y = rn.randint(-300,300)
    külgede_arv = rn.randint(3,10)
    küljepikkus = rn.randint(10,100)
    penup()
    goto(x,y)
    pendown()
    hulknurk(külgede_arv,küljepikkus)

exitonclick()