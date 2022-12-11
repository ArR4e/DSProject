from turtle import *
külgi = int(input("Sisestage külgede arv:"))
pikkus = float(input("Sisestage külje pikkus:"))
def hulknurk(külgi, pikkus):
    for x in range(külgi):
        forward(pikkus)
        left(360/külgi)
   
hulknurk(külgi, pikkus)        