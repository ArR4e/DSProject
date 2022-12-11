tekst1=str(input("Sisesta esimene failinimi:"))
tekst2=str(input("Sisesta teine failinimi:"))

f=open(tekst1)
fail=f.read()
asendused=fail.count("Hello")
tekst=fail.replace("Hello","Tere")
f.close()

z=open(tekst2, "w+")
z.write(tekst)
z.close()

print(str(asendused))
