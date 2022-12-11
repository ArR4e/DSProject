from turtle import *
from random import randint

def hulknurk():
    joonistatud_külgi = 0

    while joonistatud_külgi < 5:
        forward(randint(1,300))
        right(360/5)
        joonistatud_külgi +=1    
        

hulknurk()
turtle.begin_fill()
for joonistatud_külgi in range(30)



print(joonistatud_külgi)
exitonclick()