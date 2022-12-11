from turtle import *
import random

def hulknurk(külg,nurk):
    joonistatud_külgi = 0
    while joonistatud_külgi < külgede_arv:
        forward(külg)
        left(nurk)
        joonistatud_külgi += 1

kujundite_arv = 0        
while kujundite_arv < 30:
    külgede_arv = random.randint(3,15)
    külg = random.randint(50,100)
    sisenurkade_summa = (külgede_arv - 2) * 180
    sisenurk = sisenurkade_summa / külgede_arv
    nurk = 180 - sisenurk
    teekond = random.randint(100,400)
    pööre1 = random.randint(1,180)
    pööre2 = random.randint(180,360)
    hulknurk(külg,nurk)
    up()
    left(pööre1)
    forward(teekond)
    right(pööre2)
    down()
    kujundite_arv += 1
        

exitonclick()