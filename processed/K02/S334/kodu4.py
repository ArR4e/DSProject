a = input("Sisesta esineme fail: ")
b = input("Sisesta teine fail: ")

f = open(a)
sisu = f.read()
sisucount = sisu.count("Hello")
sisu = sisu.replace("Hello", "Tere")

f1 = open(b,"w")
f1.write(sisu)

f.close()
f1.close()

print("Tehti " + str(sisucount) + " asendamist.")


