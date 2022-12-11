uus1_fail = input("Sisestage lähtefaili nimi:")
uus2_fail = input("Sisestage sihtfaili nimi:")
f1 = open(uus1_fail)
a = f1.read()
f2 = open(uus2_fail, "w")
f2.write(a.replace("Hello", "Tere"))
print(a.count("Hello"))
f1.close()
f2.close()


