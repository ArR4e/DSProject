nimi1 = input("Palun sisestage esimese faili nimi: ")
nimi2 = input("Palun sisestage teise faili nimi: ")

ava1 = open(nimi1, "r", encoding="UTF-8")
ava2 = open(nimi2, "w", encoding="UTF-8")

sisu1 = ava1.read()
lõpp = sisu1.count("Hello")
sisu2 = ava2.writelines(sisu1.replace("Hello", "Tere"))


print (lõpp)
ava1.close()
ava2.close()