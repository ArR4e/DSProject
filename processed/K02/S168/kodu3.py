class Error (Exception):
    pass

while True:
    try: 
        eesnimi = str(input("Sisesta oma eesnimi: "))
        perenimi = str(input("Sisesta oma perenimi: "))
        if eesnimi.isalpha() == 0 or perenimi.isalpha() == 0:
            raise Error
        break
    except Error:
        print("Ees- ja perenimi ei tohi sisaldada midagi peale tähtede.")
        continue
eesnimi = eesnimi.lower()
perenimi = perenimi.lower()
eesnimi = eesnimi.replace("ü", "u")
eesnimi = eesnimi.replace("õ", "o")
eesnimi = eesnimi.replace("ö", "o")
eesnimi = eesnimi.replace("ä", "a")
perenimi = perenimi.replace("ü", "u")
perenimi = perenimi.replace("õ", "o")
perenimi = perenimi.replace("ö", "o")
perenimi = perenimi.replace("ä", "a")
print(eesnimi, perenimi, sep = '.')