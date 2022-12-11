i1 = input("Sisesta inglisekeelse faili nimi: ")
i2 = input("Sisesta eestikeelse faili nimi: ")

t1 = open(i1, "r")
inglise = t1.read()
eesti = inglise.replace("Hello","Tere")
t2 = open(i2, "w")
t2.write(eesti)
print(inglise.count("Hello"))


t1.close()
t2.close()