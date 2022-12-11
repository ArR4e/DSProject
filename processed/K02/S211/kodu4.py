f = input("sisesta sisendfaili nimi: ")
f1 = input("sisesta väljundfaili nimi: ")

f3= open(f, "r")
faili_sisu = f3.read()

faili_sisu1 = faili_sisu.replace("Hello", "Tere")

f3.close()

f4 = open(f1, "w")
f4.write(faili_sisu1)

asendus = faili_sisu.count("Hello")


f4.close()

print("Tehti",asendus,"asendust")