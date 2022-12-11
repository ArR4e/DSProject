#Hulknurgad
from turtle import *
import turtle
from random import randint

def fun(arv, pikkus):
    külgi=0
    while külgi<arv:
        forward(pikkus)
        sisenurgad=(arv-2)*180
        nurk=180-(sisenurgad/arv)
        left(nurk)
        külgi+=1
        
aken=turtle.Screen()
aken.setup(800, 800)

i=0
while i<30:
    up()
    juhuslik1=randint(10, 200)
    forward(juhuslik1)
    juhuslik_nurk=randint(1, 360)
    left(juhuslik_nurk)
    juhuslik2=randint(10, 300)
    forward(juhuslik2)
    down()
    suurus=randint(15,100)
    nurki=randint(3, 15)
    fun(nurki, suurus)
    i+=1
    
turtle.exitonclick()