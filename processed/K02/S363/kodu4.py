lähte = input("Palun sisesta oma lähtefaili nimi: ")
if ".txt" not in lähte:
    lähte = lähte + ".txt"

siht = input("Palun sisesta oma sihtfaili nimi: ")
if ".txt" not in siht:
    siht = siht + ".txt"

f = open(lähte, "r")
F = open(siht, "w")

read = f.read()
a = read.count("Hello")
read = read.replace("Hello", "Tere")

F.write(read)
print("Lähtefaili nimi: ", lähte)
print("Sihtfaili nimi: ", siht)
print("Tehti",a,"asendamist.")

F.close()
