esimene_fail = input("Sisestage lähtefaili nimi: ")
teine_fail = input("Sisestage sihtfaili nimi: ")

f1 = open(esimene_fail, "r")
f2 = open(teine_fail, "w")
failist=f1.read()

asendamised = failist.count("Hello")

lugemine= f2.write(str(failist.replace("Hello", "Tere")))

print("Tehti " + str(asendamised) + " asendamist.")

f2.close()
f1.close()