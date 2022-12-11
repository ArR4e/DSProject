e_nimi = input("Eesnimi: ")
p_nimi = input("Perenimi: ")
kasutajanimi = e_nimi.lower() + "." + p_nimi.lower()

if "ö" or "ä" or "õ" or "ü" in kasutajanimi:
    kasutajanimi = kasutajanimi.replace("ö", "o")
    kasutajanimi = kasutajanimi.replace("ü", "u")
    kasutajanimi = kasutajanimi.replace("õ", "o")
    kasutajanimi = kasutajanimi.replace("ä", "a")
    
print(kasutajanimi)