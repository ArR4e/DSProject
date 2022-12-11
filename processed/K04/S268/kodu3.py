kylgede_arv = int(input("Sisesta külgede arv: "))
kylgede_pikkus = float(input("Sisesta külgede pikkus: "))

from turtle import *

def hulknurk():
    kylgede_arv = 0
    kylgede_pikkus = 1
    while kylgede_arv < 3:
        forward(30)
        left(120)
        kylgede_arv += 1
        
hulknurk()

up()
forward(90)
left(80)
forward(90)
down()

hulknurk()
        
exitonclick()
