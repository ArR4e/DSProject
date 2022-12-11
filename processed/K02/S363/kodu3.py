eesnimi = input("Palun sisesta oma eesnimi: ").lower()
perenimi = input("Palun sisesta oma perenimi: ").lower()

kasutaja = eesnimi + "." + perenimi

if " " in kasutaja:
    kasutaja = kasutaja.replace(" ","-")
    
if "ä" or "õ" or "ö" or "ü" in kasutaja:
    kasutaja = kasutaja.replace("ä","a")
    kasutaja = kasutaja.replace("õ","o")
    kasutaja = kasutaja.replace("ö","o")
    kasutaja = kasutaja.replace("ü","u")    

print(kasutaja)