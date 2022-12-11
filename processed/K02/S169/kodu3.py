ees = input("Sisesta eesnimi: ")
pere = input("Sisesta perenimi: ")

kasutaja = (ees.lower().strip() + "." + pere.lower().strip())

for a in kasutaja:
    if a == "ö" or a == "Ö":
        kasutaja = kasutaja.replace("ö","o")
        kasutaja = kasutaja.replace("Ö", "o")
    if a == "ä" or a == "Ä":
        kasutaja = kasutaja.replace("ä","a")
        kasutaja = kasutaja.replace("Ä", "a")
    if a == "õ" or a == "Õ":
        kasutaja = kasutaja.replace("õ","o")
        kasutaja = kasutaja.replace("Õ", "o")
    if a == "ü" or a == "Ü":
        kasutaja = kasutaja.replace("Ü","y")
        kasutaja = kasutaja.replace("ü", "y")

        
    
print(kasutaja)