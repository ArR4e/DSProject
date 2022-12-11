failinimi = str(input("sisestage failinimi: "))
tulem = str(input("sisestage tulemfail: "))  
 
f = open(failinimi)
tekst = f.read()
print(failinimi.count("Hello"))


f = open(tulem, "w")
f.write((tekst).replace("Hello", "Tere"))


f.close()