f1 = input("Sisestage inglise keelse teksti failinimi: ")
f2 = input("Sisestage eesti keelse teksti failinimi: ")
fail1 = open(f1, encoding = "UTF-8")
fail2 = open(f2, "w", encoding="UTF-8")

i = 0
for rida in fail1:
    fail2.write(rida.replace("Hello", "Tere"))
    i += rida.count("Hello")

fail1.close()
fail2.close()
print(i)
