lahtefail = input("Lähtefaili nimi: ")
f1 = open(lahtefail, "r")
sihtfail = input("Sihtfaili nimi: ")
f2 = open(sihtfail, "w")
N = 0
f1 = open(lahtefail, "r")
for x in f1:
    y = x.replace("Hello", "Tere")
    f2.write(y)
    N = N + y.count("Tere")
print("Tehti " + str(N) + " asendamist.")
f1.close()
f2.close()
