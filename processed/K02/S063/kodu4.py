lahtefail = input("Sisestage lähtefaili nimi: ")
sihtfail = input("Sisestage sihtfaili nimi: ")

f = open(lahtefail)
lahtefail_sisu = f.read()
print("Lähtefaili sisu:\n"+lahtefail_sisu)
f.close()

f = open(sihtfail, "w")
f.write(lahtefail_sisu.replace("Hello", "Tere"))
f.close()

f = open(sihtfail)
sihtfail_sisu = f.read()
print("Sihtfaili sisu:\n"+sihtfail_sisu)
f.close()

print("Tehtud", lahtefail_sisu.count("Hello"), "'Hello > Tere'", "asendamist.")
