
f1 = input("Palun sisestage lähtefaili nimi:")
f2 = input("Palun sisestage sihtfaili nimi:")

f = open(f1, "r")
faili_sisu = f.read()
f.close()

l = faili_sisu.replace("Hello", "Tere")
fh = open(f2, 'w')
fh.write(l)
fh.close()

x = faili_sisu.count("Hello")
print("Tehti " + str(x) + " asendamist")
