from turtle import*
import random

def hulknurk(külgede_arv, pikkus):
    for i in range(külgede_arv):
        forward(pikkus)
        left(360/külgede_arv)
        i += 1
        
hulknurgad = 0
speed(12)

while hulknurgad < 2:
    a = random.randint(4, 10)
    b = random.randint(60, 150)
    c = random.randint(60, 150)
    d = random.randint(0, 360)
    hulknurk(a, b)
    hulknurgad += 1
    
    up()
    left(d)
    forward(b)
    down()
    
excitonclick()