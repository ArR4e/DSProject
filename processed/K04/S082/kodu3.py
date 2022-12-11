from turtle import *
from random import randint

def hulknurk(arv, pikkus):
    nurk=((arv-2)*180)/arv
    

    for i in range(0,arv):
        forward(pikkus)
        left(180-nurk)
    
      
for i in range(0,30):
    hulknurk(randint(3,10),randint(1,100))
    up()
    left(randint(0,360))
    forward(randint(1,100))
    down()
    
exitonclick()


   
    
    