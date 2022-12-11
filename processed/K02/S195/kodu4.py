
lahtf = str(input("Sisesta lähtefaili nimi: "))
sihtf = str(input("Sisesta sihtfaili nimi: "))

l = open(lahtf)
s = open(sihtf, "w+")

ingf = l.read()
asen = ingf.count('Hello')
estf = ingf.replace("Hello", "Tere")

s.write(estf)

l.close()
s.close()

print("Tehti",asen,"asendamist.")




