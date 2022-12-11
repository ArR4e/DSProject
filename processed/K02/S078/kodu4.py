x = str(input("Lähtefaili nimi: "))
y = str(input("Sihtfaili nimi: "))

print("Faili " + x + " sisu" + "\n")
engfail = open(x, encoding="UTF-8")
estfail = open(y, "w")
summ = 0
for rida in engfail:
    summ += rida.count("Hello")
    s = rida.replace("Hello", "Tere")
    estfail.write(s)
print("Tehti", summ, "asendamist")
engfail.close()
estfail.close()