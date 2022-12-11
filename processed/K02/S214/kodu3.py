eesnimi = input("Sisesta oma eesnimi: ")
perekonnanimi = input("Sisesta oma perekonnanimi: ")

nimi= eesnimi+"."+perekonnanimi
print(nimi.lower().replace('ä','a').replace('ö','o').replace('õ','o').replace('ü','u'))
