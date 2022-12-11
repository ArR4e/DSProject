
x=input("Sisesta olemasoleva faili nimi: ")
y=input("Sisesta uue faili nimi: ")

f=open((x+".txt"),"r")
f1=open((y+".txt"),"w")
for x in f.readlines():
    f1.write(x.replace("Hello","Tere"))
     
f.close()
f1.close()
#replace("Hello","Tere").