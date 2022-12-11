from turtle import *
from random import randint

def polügon():
    joonistatud_külgi = 0
    while joonistatud_külgi < n:
        forward(küljepikkus)
        left(((n - 2) * 180 / n) - 180)
        joonistatud_külgi += 1

küljepikkus = int(input("Sisesta ühe külje pikkus: "))
n = int(input("Sisesta külgede arv: "))

polügonide_arv = 0
while polügonide_arv <= 30:
    polügon()
    penup()
    goto(randint(-500,0),randint(0,500))
    pendown()
    polügonide_arv += 1
    

exitonclick()