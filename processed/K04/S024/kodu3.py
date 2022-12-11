from turtle import *
import random

n = int(input("Sisestage külgede arv: "))
a = int(input("Sisestage külje pikkus:"))

def hulknurk(n,a):
    joonistatud_külgi = 0 
    while joonistatud_külgi < n:
        forward(a)
        right(360 / n)
        joonistatud_külgi +=1

hulknurkade_arv = 0
    
while True:
    forward(a)
    right(360 / n)
    hulknurkade_arv += 1
    if hulknurkade_arv == 31:
        break
    elif hulknurkade_arv <= 30:
        up()
        setx(random.randint(-300,300))
        sety(random.randint(-300,300))
        down()
        
    
    
    

    

        

   
    
    
      

  


