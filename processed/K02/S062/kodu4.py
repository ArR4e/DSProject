lahtefail=open(input("Lähtefaili nimi: "),"r")
sihtfail=open(input("Sihtfaili nimi: "),"w")
asendusi=0
for rida in lahtefail.readlines():
    uus_rida=rida.replace("Hello","Tere")
    sihtfail.write(uus_rida)
    asendusi+=rida.count("Hello")
sihtfail.close()
print("Tehti " +str(asendusi)+ " asendamist.")