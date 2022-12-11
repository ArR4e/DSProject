x = input("Sisestage olemasolevate tekstifaili nime: ")
y = input("Sisestage uue faili nime: ")
a = (x + ".txt")
b = (y + ".txt")
print("Lähtefaili nimi: " + x + ".txt")
print("Sihtfaili nimi: " + y + ".txt")

f = open(str(a), "r")
h = open(str(y), "w")

from bingtrans import translate

ing_keeles = x
eesti_vaste = translate(ing_keeles, "en", "et")
h.write(eesti_vaste + "\n")
f.close()
h.close()

u = a.count("Hello")
print("Tehti " + str(u) + " asendamist")
