fail1 = input("sisesta 1. failinimi: ")
fail2 = input("sisesta 2. failinimi: ")

f1 = open(fail1, "r")
f2 = open(fail2, "w+")

faili_sisu = f1.read()
counter = faili_sisu.count("Hello")
f1.close()

f1 = open(fail1, "r")

for rida in f1:
    f2.write(rida.replace("Hello", "Tere"))



print("Tehti" ,counter, "asendamist")

f1.close()
f2.close()