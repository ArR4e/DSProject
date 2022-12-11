i = input("Lähtefaili nimi: ")
e = input("Sihtfaili nimi: ")

f = open(i)
ing = f.read()
arv = ing.count("Hello")
est = ing.replace("Hello", "Tere")

g = open(e, "w")
g.write(est)
f.close()
g.close()
print("Tehti " + str(arv) + " asendamist.")