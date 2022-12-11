failinimi = input("Sisesta failinimi: ")
f = open(failinimi)

failinimi2 = input("Sisesta teine failinimi: ")
f2 = open(failinimi2, "w")

summa = 0
rida1 = f.readline()
rida2 = f.readline()
rida3 = f.readline()

kordi = rida1.count("Hello")
rida1 = rida1.replace("Hello", "Tere", kordi)
f2.write(rida1)
summa = summa + kordi

kordi = rida2.count("Hello")
rida2 = rida2.replace("Hello", "Tere", kordi)
f2.write(rida2)
summa = summa + kordi

kordi = rida3.count("Hello")
rida3 = rida3.replace("Hello", "Tere", kordi)
f2.write(rida3)
summa = summa + kordi

print(summa)


f.close()
f2.close()
    