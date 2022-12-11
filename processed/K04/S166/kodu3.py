from random import *
from turtle import *
i=0
#ruut(küljepikkus,külgede arv)
def ruut(a,b):
    n = 180-(((b-2)*180)/b)
    for i in range(b):
        forward(a)
        left(n)
penup()
#setx(100)
#sety(200)
#pd()
#ruut(80,6)
#pu()
#setpos(0,0)
while i<30:
    setx(randint(-400,400))
    sety(randint(-400,400))
    pd()
    x = randint(30,60)
    y = randint(3,10)
    ruut(x,y)
    pu()
    setpos(0,0)
    i +=1



exitonclick()