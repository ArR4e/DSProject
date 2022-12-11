from turtle import *
from random import randint

while True:
    külg = int(input("Sisesta külgede arv: "))
    if külg > 2:
        break
    else:
        print("Külgede arv on liiga väike")

pikkus = float(input("Sisesta külgede pikkus: "))

speed(-1)

def hulknurk(hn_külg, hn_pikkus):
    nurk = 360 / külg
    for x in range(hn_külg):
        fd(hn_pikkus)
        rt(nurk)

for z in range(30):
    up()
    goto(randint(-400, 400), randint(-400, 400))
    down()
    hulknurk(külg, pikkus)
    
exitonclick()