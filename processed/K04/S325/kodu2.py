C = 299792.458
def summa(x,v):
    return((x+v)/(1+x*v/(C**2)))
kiirus=float(input("Esimese keha kiirus:"))
i=1
while i<4:
    a=float(input("Järgmise keha kiirus:"))
    kiirus = summa(kiirus,a)
    i += 1
print (kiirus)