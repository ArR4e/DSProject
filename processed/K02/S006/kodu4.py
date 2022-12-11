lähtefail = input("Sisesta lähtefaili nimi: ")
sihtfail = input("Sisesta sihtfaili nimi: ")

f = open(lähtefail, "r")
sisu = f.read()
hello = "Hello"
tere = "Tere"
asendused = sisu.count(hello)
f.close()

s = open(sihtfail, "w")
s.write(sisu.replace(hello,tere))
s.close()

print("Sooritati", asendused, "asendust.")