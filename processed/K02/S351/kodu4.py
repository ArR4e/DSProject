olemasolev_fail=input("Sisestage ingliskeelse faili nimi: ")
kirjutatav_fail=input("Sisestage eestikeelse faili nimi: ")

f = open(olemasolev_fail, "r")
f2 = open(kirjutatav_fail, "w")
sonu=0
for hello in f:
    sonu += hello.count("Hello")
    hello = hello.replace("Hello", "Tere")
    f2.write(hello)
    
print("Inglisekeelses failis asendati sõna ´hello´ kokku "+ str(sonu) + " korda")

f.close()
f2.close()




#f2.write(nimi + "\n")
#f2.write(vanus + "\n")
#f2.write(aadress + "\n")
#f2.close()

#print(faili_sisu)
#f.close()
