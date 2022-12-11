#a=esimene fail (olemasolev)
#b=teine fail

a=input("Sisesta esimene failinimi: ")
b=input("Sisesta teine failinimi: ")

c=open(a)

faili_sisu=c.read()

asendus=faili_sisu.replace("Hello","Tere")
print(faili_sisu.count("Hello"))

d=open(b,"w")
d.write(asendus + "\n")


c.close()
d.close()