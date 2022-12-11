fail1=input("Mis on lähtefaili nimi? ")

#https://progeopik.cs.ut.ee/02_lihtlaused.html

print("Faili sisu on:", "\n")
f=open(fail1)

tekst= f.read()
print(tekst)

asendused=tekst.count("Hello")

f.close()

fail2=input("Mis on sihtfaili nimi? ")

f=open(fail2, "w")
f.write(tekst.replace("Hello","Tere"))
f.close()

print("Sihtfaili sisu on:", "\n")
f=open(fail2)
tekst2=f.read()
print(tekst2)
f.close()

print("Kokku tehti ", asendused, " asendust.")
