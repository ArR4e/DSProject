from turtle import *
from random import uniform, randint #suvalise ujukomaarvu jaoks https://stackoverflow.com/questions/6088077/how-to-get-a-random-number-between-a-float-range

def hulknurk(a,b):
    i=0
    while i<a:
        forward(b)
        left(180-((a-2)*180)/a)
        i+=1

i=0
while i<30:
    juhuslik_külg=randint(3,10)
    juhuslik_pikkus=uniform(10,50)
    juhuslik_vahe=uniform(100,200)
    juhuslik_nurk=uniform(1,360)
    
    hulknurk(juhuslik_külg,juhuslik_pikkus)
    up()
    left(juhuslik_nurk)
    forward(juhuslik_vahe)
    down()
    i+=1
    
exitonclick()
