alg_fail = open(input("Sisesta faili nimi: "))
faili_sisu = alg_fail.read()
x = faili_sisu.replace("Hello", "Tere")
print(x)
uus_fail = input("Sisesta uue faili nimi: ")
f = open(uus_fail, "w")
f.write(x)
asendus = x.count("Tere")
print("Asendusi tehti", asendus)