eesnimi = input("Palun sisesta oma eesnimi: ").lower()
perenimi = input("Palun sisesta oma perenimi: ").lower()

eesnimi = eesnimi.replace("ü", "u")
eesnimi = eesnimi.replace("ä", "a")
eesnimi = eesnimi.replace("õ", "o")
eesnimi = eesnimi.replace("ö", "o")

perenimi = perenimi.replace("ü", "u")
perenimi = perenimi.replace("ä", "a")
perenimi = perenimi.replace("õ", "o")
perenimi = perenimi.replace("ö", "o")


print(eesnimi + "." + perenimi)