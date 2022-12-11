#Einsteini erirelatiivsusteooria
def summa(u,v):
    c = 299792.458
    return (u+v)/(1+ (u*v)/(c**2))

a1 = float(input(" Esimese keha kiirus vaatleja suhtes on:"))
a2 = float(input("Teise keha kiirus esimese keha suhtes on:"))
a3 = float(input(" Kolmanda keha kiirus teise keha suhtes on:"))
a4 = float(input("Neljanda keha kiirus kolmanda keha suhtes on:"))
print('Kiiruste summa on' ,summa(summa(summa(a1,a2),a3),a4) , 'km/s')