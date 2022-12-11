def summa(u, v):
    # valguse kiirus 299 792 458 m/s
    c = 299792.458 #km/s
    
    return (u+v)/(1+((u*v)/c**2))

while True:
    try:
        u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
        v = float(input("Teise keha kiirus esimese keha suhtes on: "))
        x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
        y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
    except:
        print("\nEi ole sobiv arv. Proovi veel.\n")
        continue
    if u < 0 or v < 0 or x < 0 or y < 0:
        print("\nSisestage positiivsed arvud.\n")
        continue
    else:
        break

print("Kiiruste summa on ", summa(summa(summa(u, v), x), y), "km/s")