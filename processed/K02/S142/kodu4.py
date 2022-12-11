lfail = input("Sisestage lähtefaili nimi:")
sfail = input("Sisestage sihtfaili nimi: ")
asendusteArv = 0

translated = []
f = open("%s" %lfail, "r")
for line in f:
    temp = line.count("Hello")
    asendusteArv += temp
    translated.append(line.replace("Hello", "Tere", temp))
f.close()

f = open("%s" %sfail, "w")
for i in range(len(translated)):
    f.write(translated[i])
f.close()

print(asendusteArv)