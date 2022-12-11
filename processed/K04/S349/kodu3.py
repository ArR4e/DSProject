from turtle import *
from random import randint

n = randint(3,20)
l = randint(1,20)

def hulknurk(n, l):
    hulknurkade_arv = 30
    for x in range (hulknurkade_arv):
        hulknurk = randint(n,l) 
        for a in range (hulknurk):
            forward(hulknurk)
            right(360 /hulknurk)
        up()
        forward(randint(1, 100))
        left(randint(1, 100))
        forward(randint(1, 100))
        down()
            

hulknurk(n, l) 


