from random import *
from turtle import *

#joonistab jorrapärase hulknurga
def hulknurk(külgede_arv, küljepikkus):
    
    joonistatud_külgi = 0
    while joonistatud_külgi < külgede_arv:
        forward(küljepikkus)
        left(360 / külgede_arv)
        joonistatud_külgi += 1

#joonistab 30 hulknurka erinevatesse kohtadesse
#+ joonistab erineva pikkuse/külgede arvuga
hulknurki = 0
while hulknurki < 30:
    #juhuslikud arvud
    juhuslik_x = randint(-400, 400)
    juhuslik_y = randint(-400, 400)
    külgede_arv = randint(3, 10)
    küljepikkus = randint(20, 45)
    
    #viib erinevasse asukohta
    up()
    goto(juhuslik_x, juhuslik_y)
    down()
    
    #joonistab funktsiooniga hulknurga
    hulknurk(külgede_arv, küljepikkus)
    hulknurki += 1

speed("fastest")
exitonclick()