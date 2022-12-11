from turtle import *
from random import *

def joonis(külgede_arv, küljepikkus):
    nurk = (külgede_arv - 2 ) * 180 / külgede_arv
    
    for i in range(külgede_arv):
        forward(küljepikkus)
        right(180-nurk)
        
def mujale(a,b):
    up()
    left(a)
    forward(b)
    down()

for i in range(30):
    külgede_arv = randint(3,10)
    küljepikkus = randint(10,30)
    
    a = randint(0,360)
    b = randint(30,100)
    
    joonis(külgede_arv,küljepikkus)
    mujale(a,b)

exitonclick()