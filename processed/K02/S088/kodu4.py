alg = input("Lahtefail: ") + ".txt"
lop = input("Sihtfail: ") + ".txt"

f = open(alg)
a = f.read()
a = a.replace("Hello", "Tere")
asendus = a.count("Tere")
print("Tehti ", asendus, " asendust.")

f2 = open(lop, "w")
f2.write(a)

f.close()
f2.close()
