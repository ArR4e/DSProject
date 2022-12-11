fail = input("sisesta olemasoleva faili nimi: ")
uus_fail= input("Sisesta uue faili nimi: ")
f = open(fail)
f2 = open(uus_fail, "w")
sisu = f.read()

x= sisu.count("Hello")
f2.write(sisu.replace("Hello", "Tere"))
print("Tehti " +str(x)+ " asendamist.")

f.close()
f2.close()