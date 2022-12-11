import random
from turtle import *

def hulknurk(kylgede_arv, kyljepikkus):
    nurk = int(180 * (int(kylgede_arv)-2)/int(kylgede arv))
    joonistatud_kylgi = 0
    while joonistatud kylgi < kylgede_arv:
        forward(kyljepikkus)
        left(nurk)
        joonistatud_kylgi += 1
    def liikumine():
        up()
        forward(n)
        left(m)
        forward(n)
        down()
            
kylgede_arv = random.random()
kyljepikkus = random.random()
n = random.random()
m = random.random()



30 * hulknurk()

exitonclick()


        

    