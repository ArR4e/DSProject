#Kehade kiiruste sisestamine
u=float(input("Sisesta siia esimese keha kiirus:"))
v=float(input("Sisesta siia teise keha kiirus:"))
x=float(input("Sisesta siia kolmanda keha kiirus:"))
y=float(input("Sisesta siia neljanda keha kiirus:"))
#Valguse kiirus
c=float(299792.458)
#Defineerin einsteini valemi
def summa (u,v):
    summa=float(( u + v)/ (1 + ((u * v)/(c ** 2))))
    return summa
uv=summa(u,v)
uvx=summa(uv,x)
uvxy=summa(uvx,y)
print("Kiiruste summa on",str(uvxy),"km/s")