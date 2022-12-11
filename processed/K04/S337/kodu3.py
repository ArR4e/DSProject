from turtle import *
import random
def kujund(n, a):
    if n <= 2:
        raise Exception("Külegde arv hulknurga joonistamiseks on liiga väike")
    s=(n-2)*180 #hulknurga sisenurkade summa
    üks = s/n #hulknurga üks sisenurk
    pööre = 180-üks #kilpkonna pööre, et sisenurka joonistada
    while n > 0:
        forward(a)
        left(pööre)
        n -= 1


x = 30 #hulknurkade arv
while x > 0:
    n=random.randint(3, 10)
    a=random.uniform(6, 20)
    kujund(n, a)
    up()
    pööre = random.randrange(1, 360, 15)
    left(pööre)
    edasi = random.randrange(int(a), int(a)+100)
    forward(edasi)
    down()
    x-=1
exitonclick()