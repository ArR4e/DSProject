from turtle import *
from math import pi
import random

kuljed = int(input("Mitme küljega hulknurki tahad? "))
pikkus = int(input("Kui pikki kulgi tahad? "))

speed(10)
delay(0)

def ruut(a,b):
    a=0
    while a < kuljed:
        forward(b)
        right(360/kuljed)
        a = a + 1
b=1
while b<31:
    ruut(kuljed, pikkus)
    right(random.randrange(0, 361, 1))
    up()
    forward(random.randrange(100, 200, 1))
    down()
    b = b + 1      
