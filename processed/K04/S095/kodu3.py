import turtle
import random

t = turtle.Turtle()
küljed = int(input('Hulknurga külgede arv: '))
pikkus = int(input('Hulknurga külgede pikkus: '))
suvaline1=random.randint(-50, 50)
suvaline2=random.randint(-50, 50)
väliminenurk = 360/küljed

def hulknurk(küljed, pikkus):
    for i in range(küljed):
        t.forward(pikkus)
        t.right(väliminenurk)
        
x=suvaline1
y=suvaline2
def positsioon(x, y):
    t.penup()
    t.goto(suvaline1, suvaline2)
    t.pendown()
    
kordused2=0
while kordused2 < 30:
    hulknurk(küljed, pikkus)
    positsioon(x, y)
    korused2=+1


# https://www.tutorialsandyou.com/python/how-to-draw-pentagon-hexagon-and-other-polygons-in-python-turtle-11.html