from turtle import *
import random

n=30



speed(0)


def lollus(arv,suurus):
    up()
    right(random.randint(1,359))
    forward(random.randint(20,150))
    down()
    for _ in range(arv):
        forward(suurus)
        right(360/arv)


for _ in range(n):
    lollus(random.randint(3,30),random.randint(10,100))


print("Tehtud!")