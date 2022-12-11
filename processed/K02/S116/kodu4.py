Lähtefail = input("Lähtefaili nimi: ")
Sihtfail = input("Sihtfaili nimi: ")

Lähte = open(Lähtefail, "rt")
Siht = open(Sihtfail, "wt")

andmed = Lähte.read()
a = andmed.count("Hello")

for line in Lähte:
    Siht.write(line.replace("Hello", "Tere"))
    
Lähte.close()
Siht.close()

print("Tehti", a, "asendamist.")