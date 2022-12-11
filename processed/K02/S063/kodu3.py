eesnimi = input("Sisestage eesnimi: ")
perenimi = input("Sisestage perenimi: ")

kasutajanimi = eesnimi+"."+perenimi
kasutajanimi = kasutajanimi.lower()
kasutajanimi = kasutajanimi.replace("ä", "a").replace("ö", "o").replace("ü", "u").replace("õ", "o")

print("Teie kasutajanimeks on:", kasutajanimi)