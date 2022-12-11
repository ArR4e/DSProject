sissefail = input("Palun sisesta sisestus faili nimi: ")
väljafail = input("Palun sisesta välja faili nimi: ")

f1 = open(sissefail)
f2 = open(väljafail, "w")

asendamised = f1.read().count("Hello")

#tekst_mod = f1.read().replace("Hello","Tere")
#tekst_mod = tekst_mod.replace("hello","tere")
#f2.write(tekst_mod)

#juhul kui tahta muuta ainult Hello ära
f2.write(f1.read().replace("Hello", "Tere"))
print(asendamised)

f1.close()
f2.close()