f = open(input("sisesta esimese faili nimi: "),"r")
g = input("sisesta teise faili nimi: ")

tekst = f.read()
asendusteArv = tekst.count("Hello")
uusTekst = tekst.replace("Hello", "Tere")
f.close()

f = open(g,"x")
f.write(uusTekst)
f.close()


print(asendusteArv)