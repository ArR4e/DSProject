f_1 = open(input("Palun sisesta lähtefaili nimi: "))

f_1_sisu = f_1.read()
print("Lähtefaili sisu:\n" + f_1_sisu)
f_1.close()

tõlgitud_f_1_sisu = f_1_sisu.replace("Hello", "Tere")

f_2 = open((input("Palun sisesta sihtfaili nimi: ")), "w+")
f_2.write(tõlgitud_f_1_sisu)
f_2.close()

n = str(f_1_sisu.count("Hello"))

print("Tehti " + n + " asendamist.")