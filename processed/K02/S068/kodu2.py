import math 

a = float(input("Sisestage liini pikkus: "))
b = float(input("Sisestage maksimaalne postide kaugus: "))
c = 0
d = 0
if a<b:
    d = d+1
c = math.ceil(a/b)+1

print(c)