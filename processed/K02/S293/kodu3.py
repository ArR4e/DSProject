eesnimi=input("Sisesta oma eesnimi: ")
perenimi=input("Sisesta oma perenimi: ")

print(eesnimi.lower().replace("ä", "a").replace("õ", "o").replace("ü", "y").replace("ö", "o")
      + "."
      + perenimi.lower().replace("ä", "a").replace("õ", "o").replace("ü", "y").replace("ö", "o"))