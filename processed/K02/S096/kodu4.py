#Masintõlge

algfail = open(input("Sisesta faili nimi: "))
sihtfail = input("Sisesta sihtfaili nimi: ")

sihtf = open(sihtfail, "w")
for i in algfail:
    sihtf.write(i.strip().replace("Hello", "Tere") + "\n")

teisendused = 0

algfail.close()
sihtf.close()

sihtf = open(sihtfail, "r")
for i in sihtf:
   teisendused += i.count("Tere")
sihtf.close()
print("Teisendused: " + str(teisendused))