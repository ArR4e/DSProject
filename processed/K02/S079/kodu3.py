# 3. Kasutajanime loomine
# Koosta programm, mis
# - küsib kasutajalt eesnime
# - küsib kasutajalt perenime
# - väljastab kasutajanime, mis on loodud eesnime ja perenime liitmisel,
# kus tähed on läbivalt väikesed ja ees- ja perenime eraldajaks on punkt.
# Kasutaja võib sisestada nime läbivalt väikeste tähtedega, ainult suurte tähtedega või segamini,
# kuid programm peab alati väljastama kasutajanime läbivalt väikeste tähtedega.

# Näide
# >>> %Run nimi.py
# Sisesta eesnimi: kALle
# Sisesta perenimi: KalDUR
# kalle.kaldur

eesnimi = input("Sisesta eesnimi: ").lower()
perekonnanimi = input("Sisesta perekonnanimi: ").lower()

print(eesnimi + "." + perekonnanimi)