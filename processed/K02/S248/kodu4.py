x=input("Sisesta olemasoleva tekstifaili nimi: ")
y=input("Sisesta uue faili nimi: ")

f=open(x)
sisu=(f.read())
f.close()


sisu2=sisu.replace("Hello", "Tere")

f2=open(y, "w")
f2.write(sisu2)
f2.close()

print((sisu).count("Hello"))
