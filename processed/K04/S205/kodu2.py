def summa(u, v):
    i=(u+v)/(1+(u*v/(s*s)))
    return float(i)
    
s=float(299792.458)

print(summa(100000,200000))

a=float(input('Esimese keha kiirus vaatleja suhtes on: '))
b=float(input('Teise keha kiirus esimese keha suhtes on: '))
c=float(input('Kolmanda keha kiirus teise suhtes on: '))
d=float(input('Neljanda keha kiirus kolmanda keha suhtes on: '))

print('Kiiruste summa on '+str(summa(summa(summa(a,b),c),d))+' km/s')

