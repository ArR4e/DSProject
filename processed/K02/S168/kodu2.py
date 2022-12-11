while True:
    try:
        liini_pikkus = int(input("Sisesta elektriliini pikkus: "))
        max_kaugus = int(input("Sisesta postide maksimaalkaugus: "))
        if liini_pikkus < 0 or max_kaugus < 0:
            print("Arvud ei tohi olla negatiivsed.")
            continue
        break
    except ValueError as e:
        print("Oops! Tekkis", e.__class__, "viga. Siseta palun kaks naturaalarvu.")
        continue
print("Poste on vaja minimaalselt:\n")
if max_kaugus > liini_pikkus:
    print(2)
else:
    if liini_pikkus % max_kaugus == 0:
        print(liini_pikkus / max_kaugus + 1) #lisame ühe, kuna liin peab ka algama postiga
    else:
        print(liini_pikkus // max_kaugus + 2)
    
    