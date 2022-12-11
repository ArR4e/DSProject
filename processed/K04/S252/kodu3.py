from turtle import *
import random

def hulknurga_küljed(külgede_arv,külje_pikkus):
    nurga_kraad = 360/külgede_arv
    loendur = 0;
    down()
    while loendur < külgede_arv:
        loendur +=1
        forward(külje_pikkus)
        right(nurga_kraad)
    up()

print (screensize())
up()
speed(0)
screensize(canvwidth=window_width()-100, canvheight=window_height()-100, bg=None)
print(screensize())
for x in range (30):
    kylgedeArv = random.randint(4,20)
    kyljePikkus = random.randint(20,100)
    xCoord = random.randint (-600,500)
    yCoord = random.randint (-200, 800)
    goto(xCoord,yCoord)
    print("Sisend: " + str(kylgedeArv)+","+ str(kyljePikkus)+", position=" +str(position()))
    hulknurga_küljed(kylgedeArv,kyljePikkus)

exitonclick()