eesnimi = input('Sisesta eesnimi: ')
perekonnanimi = input('Sisesta perekonnanimi: ')
print(eesnimi.lower().replace('ä','a').replace('ö','o').replace('ü','u').replace('õ','o') + "." + perekonnanimi.lower().replace('ä','a').replace('ö','o').replace('ü','u').replace('õ','o'))