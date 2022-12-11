pikkus = int(input("Sisesta elektriliini pikkus(m): "))
max_kaugus = int(input("Sisesta kõrvalasetsevate postide maksimaalkaugus(m): "))

if max_kaugus >= pikkus:
    min_poste = 2
    
else:
    if pikkus % max_kaugus != 0:
        min_poste = pikkus // max_kaugus + 2
    else:
        if pikkus // max_kaugus == pikkus:
            min_poste = pikkus // max_kaugus + 1
        else:
            min_poste = pikkus // max_kaugus
    #while True:
    #    kontroll = pikkus % max_kaugus
    #    if kontroll != 0:
    #        max_kaugus -= 1
    #        continue
    #    min_poste = pikkus / max_kaugus
    #    break

    
print(f"Minimaalselt läheb vaja {int(min_poste)} posti")