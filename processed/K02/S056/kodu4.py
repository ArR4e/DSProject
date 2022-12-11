esimene_fail = input("Lähtefaili nimi: ")
teine_fail = input("Sihtfaili nimi: ")

fail = open(esimene_fail,"r")
fail2 = open(teine_fail, "w")
fail3 = open(esimene_fail,"r").read()
sona = "Hello"
kogus = fail3.count(sona)
print("Tehti", kogus, " asnedamist.")
for line in fail:
    fail2.write(line.replace("Hello", "Tere"))
fail.close()
fail2.close()


#count