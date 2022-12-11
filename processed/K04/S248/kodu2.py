def summa(u,v):
    return (u+v)/(1+u*v/299792.458**2)

x=float(input("Sisesta esimese keha kiirus: "))
y=float(input("Sisesta teise keha kiirus: "))
z=float(input("Sisesta kolmanda keha kiirus: "))
q=float(input("Sisesta neljanda keha kiirus: "))

print ("Esimese keha kiirus vaatleja suhtes on: "+str(x))
print ("Teise keha kiirus esimese keha suhtes on: "+str(summa(x,y)))
print ("Kolmanda keha kiirus teise keha suhtes on: "+str(summa(y, z)))
print ("Neljanda keha kiirus kolmanda keha suhtes on: "+str(summa(z,q)))
print ("Kiiruste summa on "+str (summa(summa(summa(x,y), z), q)))

