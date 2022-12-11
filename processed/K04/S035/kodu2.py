def summa(u, v):
    return (u+v)/(1+(u*v/(299792.458**2)))
u=float(input("esimese keha kiirus vaatleja suhtes: "))
v=float(input("teise keha kiirus esimese suhtes: "))
y=float(input("kolmanda keha kiirus teise suhtes: "))
x=float(input("neljanda keha kiirus kolmanda suhtes: "))
a=summa(u, v)
b=(a+y)/(1+(a*y/(299792.458**2)))
c=(b+x)/(1+(b*x/(299792.458**2)))
print(c)

