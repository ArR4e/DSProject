#kasutajanime loomine

eesnimi = input("Sisesta oma eesnimi: ").lower()
perenimi = input("Sisesta oma perenimi: ").lower()

if "ä" in eesnimi:
    eesnimi = eesnimi.replace("ä", "a")
if "ö" in eesnimi:
    eesnimi = eesnimi.replace("ö", "o")
if "ü" in eesnimi:
    eesnimi = eesnimi.replace("ü", "u")
if "õ" in eesnimi:
    eesnimi = eesnimi.replace("õ", "o")

if "ä" in perenimi:
    perenimi = perenimi.replace("ä", "a")
if "ö" in perenimi:
    perenimi = perenimi.replace("ö", "o")
if "ü" in eesnimi:
    perenimi = perenimi.replace("ü", "u")
if "õ" in perenimi:
    perenimi = perenimi.replace("õ", "o")

print("Teie kasutajanimi on: " + eesnimi.lower() + "." + perenimi.lower())