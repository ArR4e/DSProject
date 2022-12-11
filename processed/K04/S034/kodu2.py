def summa(a,b):
    c= 299792.458 #km/s
    return (a+b)/(1+((a*b)/c**2))
    # summa1 = (a+b)/(a+((a*b)/c**2))
    
u = float(input("Palun sisesta esimene kiirus vaatleja suhtes (km/s): "))
v = float(input("Palun sisesta teise keha kiirus esimese keha suhtes (km/s) :"))
x = float(input("Palun sisesta kolmanda keha kiirus teise keha suhtes (km/s):"))
y = float(input("Palun sisesta neljanda keha kiirus kolmanda keha suhtes (km/s):"))

# kahe esimese kiiruse summa.

summa1 = summa(u,v)

# eelneva ja kolmanda keha summa.

summa2 = summa(summa1, x)

# eelneva ja neljanda keha summa.

summa3 = str(summa(summa2, y))
print("Kiiruste summa on " + str(summa3) + " km/s.")