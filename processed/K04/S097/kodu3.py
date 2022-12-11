from turtle import *

def hulknurk(külgi, pikkus):
    joonistatud_külgi = 0
    while joonistatud_külgi < külgi:
        forward(pikkus)
        right(360/külgi)
        joonistatud_külgi+=1
        
külgi=float(input("Külgi: "))
pikkus=float(input("Külje_pikkus: "))     

hulknurki=0
while hulknurki<30:
    print(hulknurk(külgi, pikkus))
    hulknurki+=1
    up()
    forward(30)
    left(35)
    forward(20)
    right(250)
    down()
    
    
exitonclick()