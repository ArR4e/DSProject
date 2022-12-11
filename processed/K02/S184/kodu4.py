fail1=input("Lähtefaili nimi:")
fail2=input("Sihtfaili nimi:")

f1=open(fail1)
r1=f1.readline()
r2=f1.readline()
r3=f1.readline()

loendus1=r1.count("Hello")
loendus2=r2.count("Hello")
loendus3=r3.count("Hello")
loendus=loendus1+loendus2+loendus3

a=r1.replace("Hello","Tere")
b=r2.replace("Hello","Tere")
c=r3.replace("Hello","Tere")

f2=open(fail2,"w")
f2.write(a)
f2.write(b)
f2.write(c)
f2.close()

print("Tehti "+str(loendus)+" asendust.")
f1.close()
