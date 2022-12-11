f=open(input("Lähtefaili nimi: "))
andmed=f.read()


f=open(input("Sihtfaili nimi: "),"w")
f.write(andmed.replace("Hello","Tere"))

#print(andmed.replace("Hello","Tere"))
asendamiste_arv=andmed.count("Hello")
print("Tehti " + str(asendamiste_arv)+" asendamist.")

f.close()