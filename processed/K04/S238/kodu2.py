def summa(u,v):
    a = (u+v) / (1 + ( u*v) / (299792.458**2))
    return a

esim = float(input("sisesta esimese keha kiirus: "))
tein = float(input("sisesta teise keha kiirus: "))
kolm = float(input("sisesta kolmanda keha kiirus: "))
neli = float(input("sisesta neljanda keha kiirus: "))

vahesumma = summa(summa(summa(esim,tein),kolm),neli)


print("Kiiruste summa on",vahesumma)