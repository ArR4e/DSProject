from turtle import*
import random
from math import*
arv=100
pikkus=50
def joonista(arv,pikkus):
    i=30
    j=0
    k=0
    while j < i:
        while k<arv:
            forward(pikkus)
            left(360/arv)
            k+=1
        up()
        random.choice([right(random.randint(1, 360)), left((random.randint(1, 360)))])
        forward(random.randint(1, 300))
        down()
        j+=1
        k=0
joonista(arv,pikkus)        
        
    