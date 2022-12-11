lahtefail = input("Lähtefaili nimi: ")
sihtfail = input("Sihtfaili nimi: ")

f = open(lahtefail, encoding = "UTF-8")

lahtefaili_sisu = f.read()

asendus= lahtefaili_sisu.count("Hello")
f.close()

f2 = open(sihtfail,"w", encoding = "UTF-8")

f2.write(lahtefaili_sisu.replace("Hello","Tere")+ "\n")

f2.close()
print("Tehti "+str(asendus)+" asendamist.")