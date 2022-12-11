from turtle import *
edge = float(input("Külgede arv: "))
length = float(input("Küljepikkus: "))
angle = 180*(edge-2)
def f():
    counter = 0
    while counter < edge:
        forward(length)
        left(180-angle/edge)
        counter+=1
f()
exitonclick()