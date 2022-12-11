fail1 = input("Failinimi, kus info on: ")
f = open(fail1, encoding = "UTF-8")

fail2 = input("Failinimi: ")
fail = open(fail2, "w")

failisisu = f.read()
asendamine = failisisu.replace("Hello", "Tere")
print(failisisu.count("Hello"))

f.close()

fail.write(asendamine)
fail.close()