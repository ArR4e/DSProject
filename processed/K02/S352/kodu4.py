fail1=input("sisestage failinimi ")
fail2=input("Sisestage uue faili nimi ")

f1=open(fail1,"r")
f2=open(fail2,"w")
tekst=f1.read()
h=tekst.count("Hello")
tekst=tekst.replace("Hello", "Tere")
print(tekst)
f2.write(tekst)

f1.close()
f2.close()

print("Tehti ", h, " asendust.")