eesnimi = input("Palun sisesta oma eesnimi: ")
perenimi = input("Palun sisesta oma perekonnanimi: ")

nimi1 = eesnimi.replace("ü" and "Ü", "u").replace("ä" and "Ä", "a").replace("õ" and "Õ", "o")\
        .replace("ö" and "Ö", "o")
nimi2 = perenimi.replace("ü" and "Ü", "u").replace("ä" and "Ä", "a").replace("õ" and "Õ", "o")\
        .replace("ö" and "Ö", "o")

print("Sinu kasutajanimi on:", nimi1.lower() + "." + nimi2.lower())