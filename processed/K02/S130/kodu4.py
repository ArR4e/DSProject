Fail1 = input("Sisestage inglise keelse faili nimi: ")
Fail2 = input("Sisestage eesti keelse faili nimi: ")

f1 = open(Fail1, "rt")
f2 = open(Fail2, "wt")

count = int(f1.read().count("Hello"))

f2.write(f1.read().replace("Hello", "Tere"))

f1.close()
f2.close()

print(count)

#https://pythonexamples.org/python-replace-string-in-file/#2 -- kasutasin seda abina.