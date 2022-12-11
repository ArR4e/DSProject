lähtefail = input("Lähtefaili nimi: ")
sihtfail = input("sihtfaili nimi: ")

f = open(lähtefail, "r")
f2 = open(sihtfail, "w")

kokku=0

for rida in f:
    f2.write(rida.replace("Hello", "Tere"))
    kokku += rida.count("Hello")

f.close()
f2.close()

print("Tehti", kokku, "asendamist.")