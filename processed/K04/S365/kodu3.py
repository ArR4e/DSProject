from turtle import*
from random import*

hulk= int(input("Hulga külgede arv täisarvuna: "))
pikkus= int(input("hulga küljepikkus pikslites täisarvuna: "))

def kujund():
    joonistatud_küljed=0
    while joonistatud_küljed < hulk:
        forward(pikkus)
        left(180-((hulk-2)*180)/hulk)
        joonistatud_küljed +=1

i=1
while i<=30:
    kujund()
    up()
    x=randint(100,300)
    y=randint(40,80)
    forward(x)
    right(y)
    down()
    i+=1


exitonclick()