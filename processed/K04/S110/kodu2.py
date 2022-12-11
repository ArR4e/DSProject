
def summa(u,v):
    
    c = 299792.458
    tehe = (u + v)/(1+(u*v)/c**2)
    return tehe
    
u = float(input('Esimese keha kiirus vaatleja suhtes: '))
v = float(input('Teise keha kiirus esimese suhtes: '))
x = float(input('Kolmanda keha kiirus teise suhtes: '))
y = float(input('Neljanda keha kiirus kolmanda suhtes: '))

summa1 = summa(u,v)
summa2 = summa(summa1,x)
summa3 = summa(summa2,y)
print('Kiiruste summa on ', str(summa3), ' km/s')