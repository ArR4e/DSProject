eesnimi = input("Sisestage oma eesnimi: ").lower()
perekonnanimi = input("Sisestage oma perekonnanimi: ").lower()

kasutajanimi = eesnimi + "." + perekonnanimi

for i in range(len(kasutajanimi)):
    if kasutajanimi[i] == "ä":
        kasutajanimi = kasutajanimi[0:i] + "a" + kasutajanimi[i+1:len(kasutajanimi)]
    elif kasutajanimi[i] == "ü":
        kasutajanimi = kasutajanimi[0:i] + "u" + kasutajanimi[i+1:len(kasutajanimi)]
    elif kasutajanimi[i] == "õ" or kasutajanimi[i] == "ö":
        kasutajanimi = kasutajanimi[0:i] + "o" + kasutajanimi[i+1:len(kasutajanimi)]

print(kasutajanimi)