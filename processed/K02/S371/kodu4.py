lähtefail = input("Lähtefaili nimi: ")
sihtfail = input("Sihtfaili nimi: ")

fail_1 = open(lähtefail, encoding = "UTF-8")
fail_2 = open(sihtfail, "w", encoding = "UTF-8")

i = 0

for rida in fail_1:
    fail_2.write(rida.replace("Hello", "Tere"))
    i += rida.count("Hello")
    
fail_1.close()
fail_2.close()
print("Tehti", i, "asendamist.")