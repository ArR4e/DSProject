from turtle import *
from random import randint

def hulknurk(n,a):
    s=(n-2)*180
    nurk=s/n
    for el in range(n):
        right(int(180-nurk))
        forward(a)

for el in range(30):
    #n=int(input("Mitme küljega kujundit soovime? "))
    #a=int(input("Sisesta soovitud korrapärase hulknurga küljepikkus: "))
    x=randint(-200,200)
    y=randint(-200,200)
    penup()
    setpos(x,y)
    pendown()
    n=randint(3,12)
    a=randint(10,50)
    hulknurk(n,a);