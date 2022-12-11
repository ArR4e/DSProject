def summa(u,v):
    vastus=(u+v)/(1+u*v/299792.458**2)
    return(vastus)
u=float(input("1 keha kiirus"))
v=float(input("2 keha kiirus"))
x=float(input("3 keha kiirus"))
y=float(input("4 keha kiirus"))
print(summa(summa(summa(u,v),x),y))