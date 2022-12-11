LähteFail = input("sisestage siia lähtefaili nimi ")
SihtFail = input("sisestage siia sihtfaili nimi ")

f = open(LähteFail)

LähteFailiSisu = f.read()
Asendused = LähteFailiSisu.count("Hello")

LähteFailiSisu = LähteFailiSisu.replace("Hello","Tere")

f2 = open(SihtFail, "w")

f2.write(LähteFailiSisu)

f.close()
f2.close()

print("Lähtefaili nimi:", LähteFail)
print("Sihtfaili nimi:", SihtFail)
print("Tehti", Asendused, "asendamist.")
