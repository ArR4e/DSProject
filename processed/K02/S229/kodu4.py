x = (input("Sisestage failinimi: "))
y = (input("Sisestage failinimi: "))
xx = open(x, "rt")
yy = open(y, "wt")
for line in xx:
    yy.write(line.replace("Hello", "Tere"))
tekst = xx.read()
z = tekst.count ("Hello")
xx.close()
yy.close()
print("Tehti " + str(z) + " asendamist.")
