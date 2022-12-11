from turtle import*
from random import randint
a = int(randint(2, 20 ))
b = float(randint(1, 200))
def hulknurk():
    joonistatud_kylgi = 0
    while joonistatud_kylgi < a:
        forward(b)
        left(360//a)
        joonistatud_kylgi += 1
hulknurk()
kordus = 0
while  kordus < 30:
    c = randint(1, 300)
    o = randint(1, 300)
    g = randint(1, 300)
    s = randint(1, 300)
    up()
    forward(c)
    left(o)
    forward(g)
    left(s)
    down()
    kordus += 1
    hulknurk()
exitonclick()
