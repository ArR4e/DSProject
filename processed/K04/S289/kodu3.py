from turtle import *
import random

def hulknurk(külgede_arv, küljepikkus):
    külgede_arv2 = külgede_arv
    while külgede_arv > 0:
        forward(küljepikkus)
        right(360/külgede_arv2)
        külgede_arv -= 1
    up()
    forward(random.randint(100, 200))
    right(random.randint(90, 180))
    down()
    
speed(15)
delay(1)
i = 0
i 
while i < 30:
        külgede_arv = random.randint(3, 10)
        küljepikkus = random.randint(20, 40)
        hulknurk(külgede_arv, küljepikkus)
        i += 1

        
exitonclick()