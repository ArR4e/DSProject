u = float(input("Sisesta esimese keha kiirus:"))
v = float(input("Sisesta teise keha kiirus:"))
x = float(input("Sisesta kolmanda keha kiirus:"))
y = float(input("Sisesta neljanda keha kiirus:"))

def summa(u,v):
    c = 299792.458
    summa = (u+v)/(1+(u*v)/c**2)
    return summa

summa(u,v)
kiirus_üks_kiirus_kaks = summa(u,v)

summa(summa(u,v),x)
kiirus_üks_kaks_kolm = summa(summa(u,v),x)

summa(v,x)
kiirus_kaks_kolm = summa(v,x)

summa(summa(summa(u,v),x),y)
kiirus_üks_kaks_kolm_neli = summa(summa(summa(u,v),x),y)

summa(x,y)
kiirus_kolm_neli = summa(x,y)

print("Esimese keha kiirus vaatleja suhtes on: " , u )
print("Teise keha kiirus esimese keha suhtes on: " , summa(u,v))
print("Kolmanda keha kiirus teise keha suhtes on: " , summa(v,x))
print("Neljanda keha kiirus kolmanda keha suhtes on: " , summa(x,y))
print("Kiiruste summa on: " , summa(summa(summa(u,v),x),y))



    
