from math import *

c = 299792.458

def summa(u, v):
    sum = u + v / 1 +u * v /c
    return

u = float(input("Sisestage esimene kiirus km/s: "))
v = float(input("Sisestage teine kiirus km/s: "))
    
    

summa(u, v)

print("Vastus on: ", summa(u,v))