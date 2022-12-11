eesnimi = input(str("Sisesta oma eesnimi: "))
perenimi = input(str("Sisesta oma perekonnanimi: "))

#### Kommentaaridena olen jätnud mõned läbiproovitud lahendused encode ja decode'st

#print(eesnimi.casefold() + "." + perenimi.casefold())

#import unicodedata
#lihtne_eesnimi = unicodedata.normalize('NFD', eesnimi).encode('ascii', 'ignore')

#utf8_eesnimi = eesnimi.encode("utf-8",errors="ignore")
#k_eesnimi = eesnimi.encode("ascii")

#encoded_eesnimi = eesnimi.encode('utf-8', errors='strict')
#decoded_eesnimi = encoded_eesnimi.decode('ascii', errors='strict')

####

import unicodedata # Lahenduse idee leidsin googlest: https://stackoverflow.com/questions/3194516/replace-special-characters-with-ascii-equivalent)

bytes_eesnimi = unicodedata.normalize('NFD', eesnimi).encode('ascii', 'ignore')
norm_eesnimi = bytes_eesnimi.decode('ascii', 'ignore')

bytes_perenimi = unicodedata.normalize('NFD', perenimi).encode('ascii', 'ignore')
norm_perenimi = bytes_perenimi.decode('ascii', 'ignore')

print(norm_eesnimi.casefold() + "." + norm_perenimi.casefold())