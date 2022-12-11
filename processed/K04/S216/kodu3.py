from turtle import *
def kujund(küljed,pikkus):
    s = (küljed-2)*180
    nurk = s/küljed 
    i = 0
    while i < küljed:
        forward(pikkus)
        left(nurk)
        i += 1
    return

küljed = int(input("Külgede arv: "))
pikkus = int(input("Küljepikkus: "))
kujund(küljed,pikkus)
    