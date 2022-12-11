#Einsteini erirelatiivsusteooria

def summa(u,v):
    c = 299792.458
    kiiruste_summa = (u+v)/(1+(u*v/c**2))
    return kiiruste_summa

kiirus_u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
kiirus_v = float(input("Teise keha kiirus vaatleja suhtes on: "))
kiirus_x = float(input("Kolmanda keha kiirus vaatleja suhtes on: "))
kiirus_y = float(input("Neljanda keha kiirus vaatleja suhtes on: "))
print("Kiiruste summa on", summa(kiirus_u,summa(kiirus_v, summa(kiirus_x,kiirus_y))) , "km/s")