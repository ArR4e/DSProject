eesnimi = input("Palun sisesta oma eesnimi: ")
perenimi = input("Palun sisesta oma perekonnanimi: ")
print(eesnimi.replace('ü', 'u').replace('ä', 'a').replace('õ', 'o').replace('ö', 'o').lower(), perenimi.replace('ü', 'u').replace('ä', 'a').replace('õ', 'o').replace('ö', 'o').lower(), sep=".")