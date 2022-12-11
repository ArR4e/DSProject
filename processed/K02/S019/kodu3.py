eesnimi = input("Mis on Teie eesimi? ")
perenimi = input ("Mis on Teie perekonnanimi? ")



kasunimi = (eesnimi.replace("ü", "u").replace("Ü", "u").replace("õ", "o").replace("Õ", "o").replace("ä", "a").replace("Ä", "a").replace("ö", "o").replace("Ö", "o").lower() + "." + perenimi.replace("ü", "u").replace("Ü", "u").replace("õ", "o").replace("Õ", "o").replace("ä", "a").replace("Ä", "a").replace("ö", "o").replace("Ö", "o").lower())

print ("Teie kasutajanimi on:", kasunimi)