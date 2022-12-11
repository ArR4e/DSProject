from turtle import *

def kujund():
    l = int(input("Sisesta küljepikkus: "))
    n = int(input("Sisesta külgede arv: "))
    for _ in range(n):
        forward(l)
        left(360/n)

for _ in range(30):
    kujund()
    up()
    forward(300)
    left(10)
    forward(250)
    down()

exitonclick()