
def summa(u, v):
    return (u+v)/(1+(u*v/(c**2)))

c=float(299792.458)
a=float(input("Sisesta esimene kiirus"))
b=float(input("Sisesta teine kiirus"))
d=float(input("Sisesta kolmas kiirus"))
e=float(input("Sisesta neljas kiirus"))

print("Esimese keha kiirus vaatleja suhten on:", a)
print("Teise keha kiirus esimese kehas suhtes on:", b-a)
print("Kolmanda keha kiirus teise keha suhtes on:", d-b)
print("Neljanda keha kiirus kolmanda keha suhtes on:", e-d)
print("Kiiruste summa on:", summa(a, summa(b, summa(d, e))), "km/s")

#summa(summa(summa(a, b), d), e)
#summa(a, summa(b, summa(d, e)))
#mõlemat pidi annab sama vastuse