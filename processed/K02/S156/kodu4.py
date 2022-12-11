fail = str(input("Sisesta lähtefailinimi: "))
fail2 = str(input("Sisesta sihtfailinimi: "))

ing = open("inglise.txt", "r")

replacement = ""
for rida in ing:
    rida = rida.strip()
    asendused = rida.replace("Hello", "Tere")
    replacement = replacement + asendused + "\n"

ing.close()

est = open("eesti.txt", "w")
est.write(replacement)
print(est.write(replacement))

est.close()

