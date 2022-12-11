f = open(input("Sisesta lähtefaili nimi: "))
inglise = f.read()
f.close()

f2 = open(input("Sisesta sihtfaili nimi: "), "w")


f2.write(inglise.replace("Hello", "Tere"))


print("Asendusi tehti: " + str(inglise.count("Hello")))
f2.close()


