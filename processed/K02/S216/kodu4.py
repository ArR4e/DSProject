
fail1 = str(input("Lähtefaili nimi: "))
fail2 = str(input("Sihtfaili nimi: "))
x = 0
lähtefail = open(fail1, encoding="UTF-8")
sihtfail = open(fail2, "w")

for rida in lähtefail:
    sõnad = rida.split()
    for s in sõnad:
        x += s.count("Hello")
    sihtfail.write(rida.replace("Hello", "Tere"))

lähtefail.close()
sihtfail.close()
print("Tehti " + str(x) + " asendamist.")








