from turtle import *
import random
speed(10)
i = 0

def hulknurk():
    a = 0
    külgede_arv = random.randint(3, 15)
    külgede_pikkus = random.randint(10, 50)
    while a < külgede_arv:
        forward(külgede_pikkus)
        right(360 / külgede_arv)
        a += 1
        
while i < 30:
    e = random.randint(-300, 300)
    r = random.randint(-300, 300)
    up()
    goto(e, r)
    down()
    hulknurk()
    i += 1
   