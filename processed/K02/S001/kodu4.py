eng = open(input("Lähtefaili nimi: "))
vanatekst = eng.read()
eng.close()

uustekst = vanatekst.replace("Hello","Tere")

est = open(input("Sihtfaili nimi: "), "w")
est.write(uustekst)
est.close()

print(vanatekst.count("Hello"))