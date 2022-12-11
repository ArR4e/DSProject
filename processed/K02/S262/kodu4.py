source = input("Lähtefaili nimi: ")
target = input("Sihtfaili nimi: ")
asendamisi = 0
algfail = open(source, encoding="UTF-8")
loppfail = open(target, "w+", encoding="UTF-8")
for rida in algfail:
    if rida.count("Hello") >= 1:
        asendamisi += rida.count("Hello")
        hetkerida = rida
        loppfail.write(hetkerida.replace("Hello","Tere"))
    else:
        loppfail.write(rida)
algfail.close()
loppfail.close()
print("Tehti " + str(asendamisi) + " asendamist.")