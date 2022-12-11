nimi1=input("Sisesta esimene faili nimi: ")
nimi2=input("Sisesta teine faili nimi: ")

f1=open(nimi1)
f2=open(nimi2, "w")

f1tekst=f1.read()
print("Tehti", f1tekst.count("Hello"), "asendamist")
f1tere=f1tekst.replace("Hello","Tere")

lõpp=f2.write(f1tere)

f1.close()
f2.close()