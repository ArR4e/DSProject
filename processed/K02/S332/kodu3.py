ees = input("Palun kirjutage oma eesnimi: ")
pere = input("Palun kirjutage oma perekonnanimi: ")
ees1 = ees.lower().replace("õ","o").replace("ä","a").replace("ü","u").replace("ö","o")
pere1 = pere.lower().replace("õ","o").replace("ä","a").replace("ü","u").replace("ö","o")
summa = ees1 + "." + pere1
print(summa)

