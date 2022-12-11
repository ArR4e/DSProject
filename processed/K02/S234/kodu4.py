nimi1=input("nimi1")
nimi2=input("nimi2")
f=open(nimi1,"r")
read=f.readlines()
f.close()
kordusi=0
uus=[]
for a in read:
    kordusi+=a.count("Hello")
    uus.append(a.replace("Hello","Tere"))
f=open(nimi2,"w")
for a in uus:
    f.write(a)
f.close()
print(kordusi)