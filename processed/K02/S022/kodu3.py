ees = input("Sisesta oma eesnimi")
pere = input("Sisesta oma perekonnanimi")
nimi = ees + "." + pere
print(nimi.replace('ä', 'a').replace('õ', 'o').replace('ü', 'y').replace('ö', 'o').lower())

