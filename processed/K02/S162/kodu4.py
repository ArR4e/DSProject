ik=input("sisesta failinimi: ")
ek=input("sisesta failinimi: ")
f=open(ik)
tekst=f.read()
x=tekst.count("Hello")
tekst=tekst.replace("Hello","Tere")
g=open(ek,"w")
g.write(tekst)
print("tehti",int(x),"asendamist")
#g=open(ek, "r")
#print(g.read())
f.close()
g.close()