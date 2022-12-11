from turtle import *
def hulknurk(arv,pikkus):
    nurk=180-(((arv-2)*180)/arv)
    while arv > 0:
        left(nurk)
        forward(pikkus)
        arv=arv-1
a=float(input("Sisestage nurkade arv:"))
b=float(input("Sisestage külje pikkus:"))
hulknurk(a,b)
