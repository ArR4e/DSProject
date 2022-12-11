eesnimi = input('Sisestage oma eesnimi ')
perekonnanimi = input('Sisestage oma perekonna nimi ')

eesnimi1 = eesnimi.lower()
eesnimi2 = eesnimi1.replace('ö','o')
eesnimi3 = eesnimi2.replace('ä','a')
eesnimi4 = eesnimi3.replace('ü','u')

perekonnanimi1 = perekonnanimi.lower()
perekonnanimi2 = perekonnanimi1.replace('ö','o')
perekonnanimi3 = perekonnanimi2.replace('ä','a')
perekonnanimi4 = perekonnanimi3.replace('ü','u')


print(eesnimi4 + '.'+ perekonnanimi4)