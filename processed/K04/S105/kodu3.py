from turtle import *
turtle=Turtle()

pikkus=float(input("Sisesta kyljepikkus: "))
kylg=int(input("Sisesta kylgede arv: "))

def hulknurk(a,b):
    
    c=((b-2)*180)
    d=c/b
    
    while b>0:
        turtle.forward(a)
        turtle.right(180-d)
        b-=1
    
hulknurk(pikkus,kylg)
