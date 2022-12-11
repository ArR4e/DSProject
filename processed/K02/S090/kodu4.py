lähtefail = input("Palun sisestage lähtefaili nimi: ")
sihtfail = input("Palun sisestage sihtfaili nimi: ")

f = open(lähtefail, "r")

loend = f.read()
sõnad = loend.replace("Hello","Tere")
arv = loend.count('Hello')
f.close()

f2 = open(sihtfail, "w")
f2.write(sõnad)
f2.close()

print("Lähtefaili nimi: "+lähtefail+".")
print("Sihtfaili nimi: "+sihtfail+".")
print("Tehti "+str(arv)+" asendamist.")


