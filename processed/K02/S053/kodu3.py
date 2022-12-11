import math
eesnimi = str(input("Sisestage oma eesnimi: "))
perenimi = str(input("Sisestage oma perenimi: "))

eesnimi_väike = eesnimi.lower()
eesnimi_ilma = eesnimi_väike.replace('ö', 'o').replace('õ', 'o').replace('ä', 'a').replace('ü', 'u')

perenimi_väike = perenimi.lower()
perenimi_ilma = perenimi_väike.replace('ö', 'o').replace('õ', 'o').replace('ä', 'a').replace('ü', 'u')

print(eesnimi_ilma, perenimi_ilma, sep=".")