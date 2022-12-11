from turtle import *

def joonista(n, l):
    a=(n-2)*180/n
    seth(0)
    while n!=0:
        forward(l)
        left(180-a)
        n-=1
        
pik=float(input("Mis on hulknurga küljepikkus?"))
arv=int(input("Mis on hulknurga külgede arv?"))

joonista(arv, pik)
