from turtle import*
import random

hulknurki = 30

while hulknurki > 0:
    hulknurki -= 1
    arv_külgi = random.randint(3, 20)
    küljepikkus = random.randint(10, 100)
    
    def hulknurk(arv_külgi, küljepikkus):
        joonistatud_külgi = 0
        
        while joonistatud_külgi < arv_külgi:
            forward(küljepikkus)
            left(360/arv_külgi)
            joonistatud_külgi += 1
        
    hulknurk(arv_külgi, küljepikkus)
    
    penup()
    left(random.randint(1, 360))
    forward(random.randint(70, 100))
    pendown()