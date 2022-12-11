# 4. Masintõlge
# Kirjuta programm, mis küsib kasutajalt kaks failinime.
# Esimene märgib mingit olemasolevat tekstifaili, teine aga mingit uut faili, mida ei tarvitse veel olemas olla.

# Programmi ülesanne on võtta esimese faili sisu, asendada seal kõik sõnad „Hello“ sõnadega „Tere“ ja
# kirjutada tulemus teise faili. Ekraanile väljastada, mitu asendamist tehti.

f_olemas = input("Lähtefaili nimi: ")
f_siht = input("Sihtfaili nimi: ")

f = open(f_olemas)
faili_sisu = f.read()
f.close()
asendused = faili_sisu.count("Hello")
uus_sisu = faili_sisu.replace("Hello", "Tere")

f_new = open(f_siht, "w")
f_new.write(uus_sisu + "\n")
f_new.close()

print("Lähtefaili nimi:", f_olemas)
print("Sihtfaili nimi:", f_siht)
print("Tehti", asendused, "asendamist.")
