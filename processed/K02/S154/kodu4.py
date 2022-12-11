failinimi = str(input("Sisestage esimene failinimi: "))
failinimi2 = str(input("Sisestage teine failinimi"))

f = open(failinimi, "r")

sisu = f.read()


print("Kokku tehti " + str(sisu.count("Hello")) + " asendamist.")

sisu = sisu.replace("Hello", "Tere")

f2 = open(failinimi2, "w")
f2.write(sisu)
print(sisu)

f.close()
f2.close()