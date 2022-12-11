from turtle import *
from random import *

def hulknurk(kylgede_arv, kyljepikkus):
    i = 0
    while i < kylgede_arv:
        forward(kyljepikkus)
        left(360/kylgede_arv)
        i += 1

speed(0)
screensize(10000, 10000)

i = 0
while i < 30:
    up()
    goto(uniform(-500, 500), uniform(-500, 500)) #juhuslike arvude vahemikke võib vajadusel muuta, hetkel valisin suvalised
    down()
    hulknurk(randint(3, 30), uniform(1, 200))
    i += 1

exitonclick()