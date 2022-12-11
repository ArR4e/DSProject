from turtle import *
from random import *

def hulknurgad(külgede_arv, külgedepikkus):
    joonistatud_külgi = 0
    while joonistatud_külgi < külgede_arv:
        forward(külgedepikkus)
        right(360/külgede_arv)
        joonistatud_külgi += 1

hulknurgadkokku = 0
while hulknurgadkokku < 30:
    hulknurgad(randint(4, 16), randint(10, 80))
    up()
    forward(randint(20, 180))
    left(randint(1, 90))
    forward(randint(1, 200))
    left(randint(1, 90))
    down()
    hulknurgadkokku += 1
    
exitonclick()
    