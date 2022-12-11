lahtefail = input("Sisesta lähtefaili nimi: ")
sihtfail = input("Sisesta sihtfaili nimi: ")

f = open(lahtefail + ".txt")
sisu = f.read()
muudatus = sisu.count('Hello')
f.close()

sisu1 = sisu.replace('Hello','Tere')

f1 = open(sihtfail + ".txt", "w")
f1.write(sisu1)
f1.close()

print("Tehti " +str(muudatus) + " muudatust")



