a = input("Palun sisestage oma failinimi (kujul - failinimi.txt): ")
b = input("Palun sisestage soovitud faili nimi (kujul - failinimi.txt): ")
f1 = open(a)

algne_tekst = f1.read()
vastus = algne_tekst.count("Hello")
Uus_tekst = algne_tekst.replace("Hello", "Tere")
f1.close()

f2 = open(b, "w")
f2.write(Uus_tekst)
f2.close()
print(vastus)

