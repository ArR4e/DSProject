from turtle import *
from random import *

def hulknurk(n, b):
    nurk = ((n-2)*180)/n
    down()
    for x in range(n):
        fd(b)
        left(180-nurk)
    up()
up()
speed(0)

#Võtab ekraani suuruse
height = window_height()
width = window_width()

for y in range(30):
    #Suvaline positsioon ekraanil
    setpos(randint(round(-height/2), round(height/2)), randint(round(-width/2), round(width/2)))
    
    #Suvaline hulknurk
    hulknurk(randint(3,20), randint(1,100))
    
done()