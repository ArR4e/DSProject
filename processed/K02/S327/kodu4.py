f = open(input("lähtefaili nimi: "))

faili_sisu = f.read()
asenduste_arv = faili_sisu.count("Hello")
faili_sisu = faili_sisu.replace("Hello" , "Tere")
f.close()

f = open(input("sihtfaili nimi: "), "w+")
f.write(faili_sisu)
f.close()
print("Tehti " + str(asenduste_arv) + " asendamist.")