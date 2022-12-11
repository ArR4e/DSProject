fail1 = input("Palun sisestage tõlgitava faili nimi: ")
fail2 = input("Palun sisestage lähtefaili nimi: ")

f1 = open(fail1)
f2 = open(fail2, "w")

m = f1.read()

#teisendati x arvu
arv = m.count("Hello")

#vahetab hello -> tere
m = m.replace("Hello", "Tere")
print('Teisendati ' + str(arv) + ' arvu.')

f1.close()

#teise faili kirjutamine
f2.write(m)
f2.close()
