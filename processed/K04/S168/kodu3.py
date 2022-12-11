from turtle import*
import random
def hulknurk(n, a):
    nurk = (180 * (n - 2)) / n
    i = 1
    pensize(4)
    while i <= n:
       left(180 - nurk)
       forward(a)
       i += 1
   
    
n = int(input("Sisestage külgede arv: "))
a = int(input("Sisestage külgede pikkus: "))
n = float(n)
a = float(a)
hulknurk(n, a)

j = 0
while j < 30:
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    n = random.randint(3, 15)
    a = random.randint(1, 100)
    penup()
    goto(x, y)
    pendown()
    hulknurk(n, a)
    j += 1
exitonclick()
    