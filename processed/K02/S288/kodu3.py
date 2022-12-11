eesnimi = input('Palun sisestage oma eesnimi: ')
perenimi = input('Palun sisestage oma perenimi: ')

kasutaja = str(eesnimi) + '.' + str(perenimi)

print('\n', '\n' + 'Teie kasutajanimi on:', kasutaja.replace('ä', 'a').replace('ö', 'o').replace('ü', 'u').replace('õ', 'o') \
      .replace('Ä', 'A').replace('Ö', 'O').replace('Ü', 'U').replace('Õ', 'O').lower())