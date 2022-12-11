from turtle import *
from random import randint

def hulknurk(u,v):
    pd()
    for i in range(u):
        forward(v)
        right(360 / u)
    up()

i = 0
speed(10)

while i < 30:
    up()
    
    ## x alates -360 ja y kuni 360 on selleks, et joonistus tuleks rohkem ekraani keskele kuna pööramine toimub alati paremale
    x = randint(-360, 180)
    y = randint(-180, 360)
    
    ## nurakade/külgede arv alates 3, sest kahe või vähema nurgaga hulknurka pole võimalik joonestada
    a = randint(3, 10)
    b = randint(50, 200)
    setpos(x, y)
    hulknurk(a, b)
    i += 1
    

exitonclick()
        
    