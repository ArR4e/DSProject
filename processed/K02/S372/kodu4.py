lähtefail = input("Sisestage lähtefaili nimi: ")
uusfail = input("Sisestage uue faili nimi: ")
fail = open(lähtefail, encoding="UTF-8")
lähtefaili_sisu = fail.read()
eestikeelne = lähtefaili_sisu.replace ("Hello", "Tere")
kogus = lähtefaili_sisu.count("Hello")
print("Tehti", str(kogus), "asendamist.")

f = open(uusfail, "w")
f.write(eestikeelne)
f.close()

