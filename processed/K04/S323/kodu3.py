from turtle import *
import random

z = 0

# nurk_kraadides = nk

    
def f(nk, a):
    nk = 360 / n
    b = 0
    while b != n: 
        forward(a)
        right(nk)
        b += 1
        if b == n: 
            break
        
while z <= 30:
    
    
    a = float(random.randint(10, 50))
    n = int(random.randint(3, 12))
    
    f(n, a)
    
    z += 1
    penup()
    setx(random.randint(-500, 500))
    sety(random.randint(-500, 500))
    pendown()
    
    if z == 30:
       
       break
