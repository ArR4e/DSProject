from turtle import *
from random import randint

külje_pikkus = int(input("Külje pikkus: "))
küljede_arv = int(input("Külgede arv: "))

n = 360 / küljede_arv

x = küljede_arv

def joonis():
    küljede_arv = 0
    while küljede_arv < x:
        forward(külje_pikkus)
        left(n)
        küljede_arv += 1
    

y = 0
while y < 3:
    speed(20)
    joonis()
    up()
    y = y + 1
    goto(randint(-300, 0), randint(0, 300))
    down()

exitonclick()