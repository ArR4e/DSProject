lähtefail=input("Sisestage lähtefaili nimi: ")
sihtfail=input("Sisestage sihtfaili nimi: ")
f1=open(lähtefail)
sisu_lähte=f1.read()
sisu_l=sisu_lähte.replace("Hello","Tere")
asendused=sisu_lähte.count("Hello")
f1.close()
f2=open(sihtfail, "w")
f2.write(sisu_l)
f2.close()
if asendused==1:
    sõne=" asendus."
else:
    sõne=" asendust."
print("Tehti " + str(asendused) + sõne)