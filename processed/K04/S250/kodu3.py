from turtle import *
import random
colormode(255)
def hulknurk(külje_pikkus,külgede_arv):
    color(random.randint(0,255),
          random.randint(0,255),
          random.randint(0,255))
    begin_fill()
    speed = 9999999999999999999999999999999999999
    delay = 0
    nurk = (360/külgede_arv) # korrapärase hulknurga puhul
                             # ((180*(külgede_arv-2))/külgede_arv) - miskipärast ei tööta korrektselt
                             # ((180*(külgede_arv-2+(1)))/külgede_arv)
    joonistatud_külgi = 0
    while joonistatud_külgi < külgede_arv:
        forward(külje_pikkus)
        left(nurk)
        joonistatud_külgi += 1
    end_fill()

i = 0
while i < 30:
    hulknurk((abs(random.randint(80,120))),(abs(random.randint(3,10))))
    r = (random.randint(1,3))
    if r == 1:
        up()
        forward(abs(random.randint(140,160)))
        down()
    if r == 2:
        up()
        left(abs(random.randint(140,160)))
        down()
    if r == 3:
        up()
        right(abs(random.randint(100,160)))
        down()
    i += 1
else:
    quit

exitonclick()
