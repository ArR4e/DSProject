lahtefaili_nimi = input("Lähtefaili nimi: ")
sihtfaili_nimi = input("Sihtfaili nimi: ")

f = open(str(lahtefaili_nimi))
lahtefaili_sisu = f.read()
asendused = lahtefaili_sisu.count("Hello")
lahtefaili_sisu_as = lahtefaili_sisu.replace('Hello', 'Tere')
print("Tehti " + str(int(asendused)) + " asendamist.")



f = open(str(sihtfaili_nimi), "w")
f.write(lahtefaili_sisu_as)


f.close()
f.close()



