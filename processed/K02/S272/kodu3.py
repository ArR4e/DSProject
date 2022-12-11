nimi = str(input("Sisestage oma nime:"))
pere = str(input("Sisestage oma perekonanime:"))
kasu = nimi.lower().replace("ö","o").replace("ä","a").replace("ü","u").replace("õ","o")+"."+pere.lower().replace("ö","o").replace("ä","a").replace("ü","u").replace("õ","o")
print ("Teie kasutajanimi on: " + kasu)