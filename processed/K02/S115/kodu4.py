failinimi_kust = input("Lähtefaili nimi: ")
failinimi_kuhu = input("Sihtfaili nimi: ")

f = open(failinimi_kust)
failisisu = f.read()

f = open(failinimi_kuhu, "w")
f.write(failisisu.replace("Hello", "Tere") + "\n")

print("Tehti " + str(failisisu.count("Hello")) + " astendamist.")

f.close()