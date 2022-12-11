def summa(u,v):
    c=299792.458
    return (u+v)/(1+u*v/c**2)
    
u=float(input("Sisesta esimese keha kiirus:"))
v=float(input("Sisesta teise keha kiirus:"))
x=float(input("Sisesta kolmanda keha kiirus:"))
y=float(input("Sisesta neljanda keha kiirus:"))
print(summa(summa(summa(u,v),x),y))
   
   