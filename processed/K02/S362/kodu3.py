eesnimi=input("Sisesta eesnimi: ")
perenimi=input("Sisesta perenimi: ")
kasutajanimi=((eesnimi + "."+ perenimi).replace('ä','a')).lower()
print(str(kasutajanimi))