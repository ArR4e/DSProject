eesnimi = input("Sisesta oma eesnimi: ")
perenimi = input("Sisesta oma perekonnanimi: ")
print("Sinu kasutajanimi on: " + eesnimi.lower().replace(' ', '').replace('-','').replace('õ','o').replace('ö','o').replace('ü','u').replace('ä','a') + "." + perenimi.lower().replace('õ','o').replace('ö','o').replace('ü','u').replace('ä','a'))