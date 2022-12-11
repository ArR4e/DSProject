from random import *
from turtle import *

def hulknurgad(kylgede_arv,kyljepikkus):
    joonistatud_kylgi=0
    
    while joonistatud_kylgi < kylgede_arv:
        forward(kyljepikkus)
        nurk=360/kylgede_arv
        left(nurk)
        joonistatud_kylgi += 1
i=30   
while i>0:
    kylgede_arv=int(uniform(1,50))
    kyljepikkus=uniform(10,50)
    
    hulknurgad(kylgede_arv,kyljepikkus)
    
    edasi=uniform(1,100)
    kraade=uniform(1,360)
    up()
    forward(edasi)
    left(kraade)
    forward(edasi)
    down()
    
    i=i-1
    


#uniform(x,y) x ja y väärtuste vahemik