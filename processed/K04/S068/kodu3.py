from turtle import *
from random import *
b=30
arv=0
pikkus=0

def hulknurk (arv,pikkus):
    nurk=(randrange(3,50))
    arv=(float(360/nurk))
    pikkus=(int(15+(randrange(1,20))))
    while nurk>0:
        nurk-=1
        forward(pikkus)
        left(arv)
        
def koht ():
    up()
    forward(randrange(20,100))
    right(randrange(1,360))
    forward(randrange(20,100))
    down()        
    
while b>0:
    hulknurk(arv,pikkus)
    koht()
    b-=1

exitonclick()