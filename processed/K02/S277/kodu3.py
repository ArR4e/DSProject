eesnimi = input('Sisestage oma eesnimi: ')
perenimi = input('Sisestage oma perenimi: ')
kasutaja = str.lower(eesnimi +'.'+ perenimi)
print(kasutaja.replace('ä', 'a').replace('ö', 'o').replace('ü', 'u').replace('õ', 'o'))