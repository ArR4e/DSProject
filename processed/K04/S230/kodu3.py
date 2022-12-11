from turtle import*
from random import randint
n=0
speed(0)
def hulknurk(arv, mõõt):
    i=0
    while(i<arv):
        i+=1
        forward(mõõt)
        right(180-(((arv-2)*180)/arv))

while(n<30):
    n+=1
    down()
    hulknurk(randint(3,10),randint(10,100))
    up()
    goto(randint(-800, 800),randint(-300,400))


exitonclick()
