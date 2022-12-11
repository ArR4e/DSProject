#  u+v / 1 + ( u*v / c**2 )
# c valguse kiirus (299792.458km/s)
k=299792.458
summaarum=0
def summa(u,v):
    o=(u+v)/(1+(u*v)/(k**2))
    return o
a=float(input("Sisesta esimene kiirus: "))
b=float(input("Sisesta teine kiirus: "))
c=float(input("Sisesta kolmas kiirus: "))
d=float(input("Sisesta neljas kiirus: "))
print("Esimese keha kiirus vaatleja suhtes on: "+str(summa(a,b)))
o=summa(a,b)
print("Teise keha kiirus esimese keha suhtes on: "+str(summa(o,b)))
o=summa(o,b)
print("Kolmanda keha kiirus teise keha suhtes on: "+str(summa(o,c)))
o=summa(o,c)
print("Neljanda keha kiirus kolmanda keha suhtes on: "+str(summa(o,d)))
o=summa(o,d)
print("Kiiruste summa on: "+str(summa(o,a))+"km/s")
#NB! ma tean väga hästi, et see kirjapilt on kohutav aga ma hetkel
# ei suutnud paremat varianti välja nuputada