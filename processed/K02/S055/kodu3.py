eesnimi = input("Sisesta eesnimi: ")
perenimi = input("Sisesta perenimi: ")

kasutajanimi = eesnimi.lower() + "." + perenimi.lower()

kasutajanimi = kasutajanimi.replace("õ","o")
kasutajanimi = kasutajanimi.replace("ä","a")
kasutajanimi = kasutajanimi.replace("ö","o")
kasutajanimi = kasutajanimi.replace("ü","u")

print(kasutajanimi)
