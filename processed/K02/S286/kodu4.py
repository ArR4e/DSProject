lfail = str(input("Sisesta lähtefaili nimi: "))

sfail = str(input("Sisesta sihtfaili nimi: "))


algfail = open(lfail,"r")
tekst = algfail.read()
tekst = tekst.replace("hello", "tere")
tekst = tekst.replace("Hello", "Tere")
üksustearv = tekst.count("Tere")
üksustearv += tekst.count("tere")
print(üksustearv)
uusfail = open(sfail, "w")
uusfail.write(tekst)
uusfail.close()