ees = input("Sisestage oma eesnimi: ")
pere = input("Sisestage oma perekonnanimi: ")


kasutaja = ees.casefold() + "." + pere.casefold()
kasutaja = kasutaja.replace(" ", "").replace("ä", "a").replace("ö", "o").replace("õ", "o").replace("ü", "u")


print(kasutaja)