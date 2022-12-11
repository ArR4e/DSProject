eesnimi = input("Sisesta eesnimi: ")
perenimi = input("Sisesta perenimi: ")

kasutaja = eesnimi.lower() + "." + perenimi.lower()

for i in kasutaja:
    if i == "õ" or i == "ö":
        i = "o"
# Ei suutnud välja mõelda ilusat lahendust, kuidas see n-ö tähe asendus toimuks.
# Ilma selleta, et hakkaks sõnet poolitama ja siis tagasi kokku toppima.
    if i == "ü":
        i = "u"
        
    if i == "ä":
        i = "a"

print(kasutaja)