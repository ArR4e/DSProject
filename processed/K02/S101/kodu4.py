


esialgne_tekstifail= input("sisestage lähtefaili nimi:")
uus_tekstifail= input("sisestage sihtfaili nimi:")
f=open(esialgne_tekstifail)
sisu=str(f.read())
sisu2=sisu.replace("hello","tere")
sisu3= sisu2.replace("Hello","Tere")
sisu.replace("Hello","Tere")
print("algfaili sisu:")
print(sisu+"\n")
k = open(uus_tekstifail,"w")

k.write(sisu3)


print("tõlgitud faili sisu:")
print(sisu3)



print("asendusi tehti:",sisu.count("hello")+sisu.count("Hello"))
f.close()
k.close()