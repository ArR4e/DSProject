#Mirjampirn
from tkinter import *
from turtle import*
from random import randint

def joonista_hulknurk(kylgede_arv,kyljepikkus):
    sisenurk=(kylgede_arv-2)*180
    keeramine=360/kylgede_arv
    for kylg in range(0,kylgede_arv):
        forward(kyljepikkus)
        right(keeramine)

kylgede_arv=int(input("Palun sisestage külgede arv: "))
kyljepikkus=int(input("Palun sisestage külje pikkus: "))

joonista_hulknurk(kylgede_arv,kyljepikkus)

for i in range (0, 60):
    koht1=randint(-600,600)+1
    koht2=randint(-300,300)+1
    penup()
    goto(koht1,koht2)
    pendown()
    kylje_pikkus1=randint(0,300)
    kylgede_arv1=randint(0,30)
    joonista_hulknurk(kylgede_arv1,kylje_pikkus1)
    
exitonclick()