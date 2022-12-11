def tapitahed(sona):
    if "ä" in sona:
        sona = sona.replace("ä", "a")
    if "õ" in sona:
        sona = sona.replace("õ", "o")
    if "ö" in sona:
        sona = sona.replace("ö", "o")
    if "ü" in sona:
        sona = sona.replace("ü", "u")
    
        
    return sona



ees = str(input("Sisesta oma eesnimi: ")).lower()
pere = str(input("Sisesta oma perekonnanimi: ")).lower()



print(tapitahed(ees) + "." + tapitahed(pere))