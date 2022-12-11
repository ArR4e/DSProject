from turtle import *
from random import randint

def f(n, a):
    i = 0
    while i != n:
        forward(a)
        right(180-((n-2)*180)/n)
        i += 1
        
for i in range(30):
    up()
    setposition(randint(-300,300),randint(-300,300))
    down()                                    
    f(randint(3, 10),randint(10, 100))        
        
exitonclick()