l= input("Sisesta lähtefaili nimi: ")
s= input("Sisesta sihtfaili nimi: ")
lahe= open(l, "r")
sisu= lahe.read()
lahe.close()
arv= sisu.count("Hello" or "hello")
sisu=sisu.replace("Hello", "Tere")
siht= open(s,"a")
siht.write(sisu)
siht.close()
print("Tehti " + str(arv) + " asendamist.")