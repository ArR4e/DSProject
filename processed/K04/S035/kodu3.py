from turtle import *
from random import randint
n=randint(1, 100)
s=randint(1, 100)
def kujund(n,s):
    joonistatud_kylgi = 0
    while joonistatud_kylgi < n:
        forward(s)
        left(180-((n-2)*180/n))
        joonistatud_kylgi += 1
a=0
while a<=30:
    kujund(n,s)
    up()
    goto(randint(-100,0),randint(0,100))
    down()
    a+=1