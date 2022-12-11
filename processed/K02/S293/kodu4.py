lähte=input("Sisesta lähtefaili nimi: ")
siht=input("Sisesta sihtfaili nimi: ")

flähte=open(lähte, "r")
fsiht=open(siht, "w")

flähtesisu=flähte.read()
fsiht.write(flähtesisu.replace("Hello", "Tere"))


muudatused=flähtesisu.count("Hello")
print("Tehti", str(muudatused), "muudatust.")

flähte.close()
fsiht.close()
