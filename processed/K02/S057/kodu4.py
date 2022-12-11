alg = input("Sisestage olemasoleva tekstifaili nimi: ")
lõpp = input("Sisestage uue tekstifaili nimi: ")

f = open("inglise.txt")
algfaili_tekst = f.read()
print("Algfaili tekst:", algfaili_tekst)


g = open("eesti.txt")
lõppfaili_tekst = f.read()
lõppfaili_tekst.replace("Hello", "Tere")
print("Tehti", lõppfaili_tekst.count("Tere"),"asendust.")