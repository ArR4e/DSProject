eesnimi = str(input("Sisestage oma eesnimi: "))
perenimi = str(input("Sisestage oma perekonnanimi: "))

kasutajanimi = (eesnimi.lower() + "." + perenimi.lower()).replace("õ","o").replace("ö","o").replace("ä","a").replace("ü","u")

print(kasutajanimi)