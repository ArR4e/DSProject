pikkus = int(input("Sisesta liini pikkus: "))
kaugus = int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus: "))
kogus = pikkus / kaugus
jääk = pikkus % kaugus
if jääk == 0:
    print("Vaja läheb minimaalselt",int(kogus) + 1,"posti",sep=" ")
else:
    print("Vaja läheb minimaalselt",int(kogus) + 2,"posti",sep=" ")