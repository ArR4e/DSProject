pikkus = int(input("Sisesta liini pikkus: "))
max_kaugus = int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus: "))
if pikkus == max_kaugus:
    print("2")
elif pikkus//max_kaugus==pikkus:
    x = pikkus//max_kaugus
    print(x+1)
else:
    x = pikkus//max_kaugus
    postide_arv = x+2
    print(postide_arv)