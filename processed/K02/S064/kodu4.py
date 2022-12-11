lähtefail = str(input("Lähtefaili nimi: "))
sihtfail = str(input("Sihtfaili nimi: "))

esimene_fail = open(lähtefail, "r")
tekst = esimene_fail.read()
inglise = "Hello"
eesti = "Tere"

asendamine = tekst.count(inglise)
esimene_fail.close()

teine_fail = open(sihtfail, "w")
teine_fail.write(tekst.replace(inglise, eesti))
teine_fail.close()

print("Tehti", asendamine, "asendamist.")




