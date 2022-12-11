from turtle import *
from random import randint
import time
speed(9)
def hulknurk(kylgede_arv, kylje_pikkus):
    nurk =  360 / kylgede_arv
    for i in range(kylgede_arv):
        fd(kylje_pikkus)
        left(nurk)
    
for i in range(30):
    up()
    goto(randint(-(1920//2),1920//2), randint(-(1080//3), 1080//3))
    down()
    hulknurk(randint(3, 9), randint(20, 70))


exitonclick()

