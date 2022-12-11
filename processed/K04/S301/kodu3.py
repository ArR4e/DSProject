from turtle import *
from random import randint
from math import pi, degrees
def hulknurk(n, y):
    nurkade_arv = n
    sisenurkade_summa = degrees((nurkade_arv-2) * pi)
    kyljepikkus = y
    nurk = 180 - sisenurkade_summa / n
    while n > 0:
        forward(kyljepikkus)
        left(nurk)
        n-= 1
        
       
def liigu_mujale(a, b):
    up()
    forward(a)
    left(b)
    backward(a)
    right(b)
    down()
    

i = 30
while i > 0:
    a = randint(1, 40)
    b = randint(1, 360)
    n = randint(3, 8)
    y = randint(1, 35)
    liigu_mujale(a, b)
    hulknurk(n,y)    
    i-= 1
    
        
exitonclick()
