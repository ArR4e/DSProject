faili_nimi = input("Sisestage olemasoleva faili nimi: ")
uue_faili_nimi = input("Sisestage uue faili nimi: ")

olemasolev_fail = open(faili_nimi, "r")
sisu = olemasolev_fail.read()
print("Lähtefaili nimi: " + faili_nimi)
print("Sihtfaili nimi: " + uue_faili_nimi +"\n")
print("Lähtefaili sisu: ")
print(sisu + "\n\n")

muudetud_sisu = sisu.replace("Hello", "Tere")
print("Tehti " + str(sisu.count("Hello")) + " asendamist.\n\n")

uus_fail = open(uue_faili_nimi, "x")
uus_fail = open(uue_faili_nimi, "w")
uus_fail.write(muudetud_sisu)

uus_fail = open(uue_faili_nimi, "r")
uue_faili_sisu = uus_fail.read()

print("Sihtfaili sisu: ")
print(uue_faili_sisu)