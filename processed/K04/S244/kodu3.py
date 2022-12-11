from turtle import *

def hulknurk(arv, pikkus):
    muutuja = 0
    while muutuja < 30:
        for x in range(arv):
            forward(pikkus)
            right(360 / arv)
        up()
        forward(50)
        left(90)
        forward(50)
        right(90)
        forward(100)
        down()
        muutuja += 1
        
    
arv = int(input("Sisesta külgede arv: "))
pikkus = int(input("Sisesta külgede pikkus: "))

hulknurk(arv, pikkus)