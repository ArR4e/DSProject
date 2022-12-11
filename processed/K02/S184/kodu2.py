from math import*
p=input("Kui pikk on elektriliin?")
pikkus=int(p)
pikk=round(pikkus)
v=input("Kui suur on vahe kahe posti vahel?")
vahe=int(v)
va=round(vahe)
if pikk<va:
   print("2")
else:
    arv=pikk/va+1
    a=ceil(arv)
    print(a)
