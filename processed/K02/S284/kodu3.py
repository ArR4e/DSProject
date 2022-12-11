a = input("Palun sisesta enda eesnimi:").lower().replace("ö", "o").replace("ä", "a").replace("ü", "u").replace("õ", "o")
b = input("Palun sisesta enda perenimi:").lower().replace("ö", "o").replace("ä", "a").replace("ü", "u").replace("õ", "o")
print("Sinu kasutajanimi on " + a + "." + b)