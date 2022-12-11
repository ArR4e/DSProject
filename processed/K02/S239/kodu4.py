esimene_fail=input("Palun sisesta olemasoleva faili nimi: ")
teine_fail=input("Palun sisesta uue faili nimi: ")

f=open(esimene_fail)
tekst=f.read()
tere1=int(tekst.count("Tere"))
tere2=int(tekst.count("tere"))

g=open(teine_fail, "w")
g.write(tekst.replace("Hello","Tere").replace("hello","tere")+"\n")
g.close()

g=open(teine_fail)
tekst2=g.read()
asendus1=int(tekst2.count("Tere"))
asendus2=int(tekst2.count("tere"))
print("Tehti "+str((asendus1+asendus2)-(tere1+tere2))+" asendamist")
g.close()
