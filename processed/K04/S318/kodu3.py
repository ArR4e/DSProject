from turtle import *
from random import *
rand_nurk=randint(3,20)
rand_kylg=randint(20,60)

def hulknurk(nurk,kylg):

    for h in range(30):
        for i in range(nurk):
            angle=360/nurk
            forward(kylg)
            left(angle)
        penup()
        right(randint(0,360))
        forward(randint(20,70))
        pendown()
print(hulknurk(rand_nurk, rand_kylg))