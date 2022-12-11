Failinimi1=input("sisesta faili nimi:")
Failinimi2=input("sisesta faili nimi:")

f=open(Failinimi1)
f1=f.read()
print("Tehti",f1.count("Hello"),"asendamist")
f1tõlge=f1.replace("Hello","Tere")
f.close()

g=open(Failinimi2,"w")
g.write(f1tõlge)
g.close()