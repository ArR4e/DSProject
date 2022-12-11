# Hulknurgad
import turtle 

def hulknurk(n,pikkus):
    for i in range(n):
        turtle.fd(pikkus)
        turtle.rt(360/n)
        
        
n = 30
pikkus = 20

hulknurk(n,pikkus)
exitonclick()
