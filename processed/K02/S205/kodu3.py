
eesnimi=str(input('Sisesta eesnimi:'))
perekonnanimi = str(input('Sisesta perenimi:'))
kasutajanimi_uni = eesnimi.lower()+ '.' + perekonnanimi.lower()
kasutajanimi = kasutajanimi_uni.replace('ä','a').replace('ö','o').replace('õ','o').replace('ü','u')

print(kasutajanimi)