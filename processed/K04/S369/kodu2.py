c = float(299792.458)

#Valem 2 kiiruse summa arvutamiseks
def summa(u, v):
    return (float(u+v)/(1+((u*v)/c**2)))

kiirus1 = float(input("Sisesta esimese keha liikumise kiirus(km/s)"))
kiirus2 = float(input("Sisesta teise keha liikumise kiirus(km/s)"))
kiirus3 = float(input("Sisesta kolmanda keha liikumise kiirus(km/s)"))
kiirus4 = float(input("Sisesta neljanda keha liikumise kiirus(km/s)"))

    
print("Kiiruste summa on: ",summa(summa(summa(kiirus1, kiirus2), kiirus3), kiirus4), "km/s")
    
    