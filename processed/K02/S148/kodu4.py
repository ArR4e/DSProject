lähtefail = input("Lähtefaili nimi: ")
sihtfail = input("Sihtfaili nimi: ")

fail_1 = open(lähtefail)
sisu_1 = fail_1.read()
fail_1.close()

asendused = sisu_1.count("Hello")
sisu_2 = sisu_1.replace("Hello", "Tere")

fail_2 = open(sihtfail, "w")
fail_2.write(sisu_2)
fail_2.close()

print("Tehti ", asendused, " asendust.")