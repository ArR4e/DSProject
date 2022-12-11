from turtle import *
from random import randint

def hulknurk(külgede_arv, küljepikkus):
    joonistatud_külgi = 0
    while joonistatud_külgi < külgede_arv:
        forward(küljepikkus)
        right(360/külgede_arv)
        joonistatud_külgi += 1
    
i = 0
while i < 30:
    speed(8)
    hulknurk(randint(3, 10), randint(20, 80))
    up()
    goto(randint(-300, 300), randint(-300, 300))
    down()
    i += 1

exitonclick()

#Sain natuke inspiratsiooni kahel veebilehelt:
#https://geektechstuff.com/2018/04/29/random-turtle-shapes-python/
#https://geeksforgeeks.org/draw-any-polygon-in-turtle-python/