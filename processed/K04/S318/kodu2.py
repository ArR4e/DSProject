es = float(input("Esimese keha kiirus vaatleja suhtes on: "))
te = float(input("Teise keha kiirus esimese keha suhtes on: "))
ko = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
ne = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

def summa(u,v):
    if type(u) and type(v) == "float" or "int":
        c = 299792.458
        kiirus = (u+v)/(1+(u*v)/c**2)
        return kiirus

    else:
        raise ValueError("Sisendid peavad olema arvud")
print(str(summa(summa(summa(es,te),ko),ne))+" km/s")