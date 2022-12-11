liinipikkus = int(input("Sisesta liini pikkus: "))
#print(liinipikkus)
kaugus = int(input("Sisesta kõrvalasetsevate postide maksimaalkaugus: "))
kaugus01 = int(input("Sisesta postide kaugus: "))
if kaugus > kaugus01:
    print(int(liinipikkus/kaugus01 +1))
else:
    print(int(liinipikkus/kaugus + 1))