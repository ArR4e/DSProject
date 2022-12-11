from turtle import *

külgede_arv = int(input("Sisestage külgede arv: "))
küljepikkus = int(input("Sisestage küljepikkus: "))
i = 0
nurk = 180 -(((külgede_arv - 2) * 180) / külgede_arv)

while i < külgede_arv:

    #def f(külgede_arv, küljepikkus):
        
    forward(küljepikkus)
    left(nurk)
    i = i + 1