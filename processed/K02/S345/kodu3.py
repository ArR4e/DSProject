eesnimi = input("Sisestage oma eesnimi: ")
perenimi = input("Sisestage oma perekonnanimi: ")

kasutajanimi = (eesnimi.lower() + "." + perenimi.lower())
print(kasutajanimi.replace("õ", "o").replace("ö", "o").replace("ä", "a").replace("ü", "u"))