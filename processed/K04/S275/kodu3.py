from turtle import *
import random



a = int(input("Sisestage külgede arv: "))
b = int(input("Sisestage küljepikkus: "))

def hulknurk(x, y):
    kraadid = ((180 * x)/x) + 180
    joonistatud_kylgi = 0
    while joonistatud_kylgi < x:
        forward(y)
        right(kraadid/x)
        joonistatud_kylgi += 1

    
for i in range(30):
    hulknurk(a, b)
    penup()
    goto(random.randint(-300, 300), random.randint(-300, 300))
    pendown()


    
    
    