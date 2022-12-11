enimi = input("Palun sisesta oma eesnimi ja vajuta ENTER: ")
pnimi = input("Palun sisesta oma perekonnanimi ja vajuta ENTER: ")
kasutajanimi = enimi.lower().replace('ä','a').replace('ö','o').replace('õ','o').replace('ü','u')+'.'+pnimi.lower().replace('ä','a').replace('ö','o').replace('õ','o').replace('ü','u')
print("Teie kasutajanimi on: " + kasutajanimi)
