eesnimi = input("Sisesta oma eesnimi: ")
perenimi = input("Sisesta oma perekonnanimi: ")

eesnimi.replace("Ä", "a")
eesnimi.replace("Ü", "u")
eesnimi.replace("Õ", "o")
eesnimi.replace("Ö", "o")

perenimi.replace("Ä", "a")
perenimi.replace("Ü", "u")
perenimi.replace("Õ", "o")
perenimi.replace("Ö", "o")

print("Kasutajanimi: ", eesnimi.lower()+"."+perenimi.lower())
