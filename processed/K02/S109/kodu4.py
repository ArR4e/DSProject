lähtefail = input("Lähtefaili nimi: ")
sihtfail = input("Sihtfaili nimi: ")

fail = open(lähtefail)
tekst = fail.read()
a = tekst.count("Hello")

print("Tehti " + str(a) + " asendamist.")