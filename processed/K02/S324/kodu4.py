fail_1 = input("Palun sisesta lähtefaili nimi: ")
fail_2 = input("Palun sisesta sihtfaili nimi: ")

f_1 = open(fail_1)
sisu_1 = f_1.read()
f_1.close()

f_2 = open(fail_2, "w")
f_2.write(sisu_1.replace("Hello", "Tere"))
f_2.close()

teisendused = sisu_1.count("Hello")


print("Tehti " + str(teisendused) + " asendamist!")