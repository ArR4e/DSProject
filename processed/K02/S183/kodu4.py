Lahte = input("Lähtefaili nimi: ")
Siht = input("Sihtfaili nimi: ")

fail = open(Lahte, encoding="UTF- 8")
faili_sisu = fail.read()
hello = faili_sisu.count("Hello")
muutuma = faili_sisu.replace("Hello", "Tere")

f = open(Siht, "w")
f.write(muutuma + "\n")


print("Tehti " + str(hello) + " asendamist.")

f.close()
fail.close()