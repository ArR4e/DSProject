from turtle import *

a = int(input("Küljepikkus: "))
b = 0

while b <= 30:
    forward(a)
    left(12)
    b += 1
    
exitonclick()