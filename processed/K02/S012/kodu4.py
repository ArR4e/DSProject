a = input("Sisesta lähtefaili nimi: ")
b = input("Sisesta sihtfaili nimi: ")
lähtef = open(a, "r")
sihtf = open(b, "w")
sihtf.write(lähtef.readline().replace("Hello","Tere"))
lähtef.close()
sihtf.close()

teisendusf = open(b, "r")
teisendus = teisendusf.readline().count("Tere")
print("Tehti " + str(int(teisendus)) + " asendust")
lähtef.close()
sihtf.close()




