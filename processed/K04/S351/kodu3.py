from random import randint
from turtle import *

def joonista(kylgede_arv, kylje_pikkus):
    kraade=(kylgede_arv-2)*180
    nurk=180-(kraade/kylgede_arv)
    x=randint(-500,500)
    y=randint(-500,500)
    up()
    setpos(x,y)
    down()
    for i in range(kylgede_arv):
        forward(kylje_pikkus)
        right(nurk)

i=1       
while i<=30:
    kylgede_arv=randint(3,10)
    kylje_pikkus=randint(10,100)  
    joonista(kylgede_arv, kylje_pikkus)
    i+=1
    
    

