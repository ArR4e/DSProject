eesnimi = str(input("Sisesta oma eesnimi: "))
perenimi = str(input("Sisesta oma perekonnanimi: "))

eesnimi

print("Sinu kasutajanimi on " + eesnimi.lower().replace("õ", "6").replace("ä", "2").replace("ö","o").replace("ü", "y") \
      + "." + perenimi.lower().replace("õ", "6").replace("ä", "2").replace("ö","o").replace("ü", "y"))