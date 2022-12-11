#KN
ees = input("Sisesta eesnimi: ").lower().replace('õ', 'o').replace('ä','a').replace('ö','o').replace('ü','u')
pere = input("Sisesta perenimi: ").lower().replace('õ', 'o').replace('ä','a').replace('ö','o').replace('ü','u')
kasutajanimi = ees + "." + pere
print(kasutajanimi)
