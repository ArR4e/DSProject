f = open(input("Lähtefaili nimi: "))

print("\n")

faili_sisu = f.read()
print("Lähtefaili sisu: " + "\n" + faili_sisu)

f.close()

print("\n")

f = input("Sihtfaili nimi: ")
f = open(f, "w")

t6lge = faili_sisu.replace("Hello","Tere")
f.write(t6lge)

print("\n")

print("Sihtfaili sisu: " + "\n" + t6lge)

print("\n")

print("Tehti ", faili_sisu.count("Hello"), "asendamist.")

f.close()