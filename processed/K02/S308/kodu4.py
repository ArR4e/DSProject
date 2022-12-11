fe=input("Sisestage eestikeelne failinimi:")
fi=input("Sisestage ingliskeelne failinimi:")

f1=open(fe)
f2=open(fi, "w")

i=0
for rida in f1:
    f2.write(rida.replace("Hello", "Tere"))
    i+=rida.count("Hello")

f1.close()
f2.close()
print(i)