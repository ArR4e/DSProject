fail_eng = input("Sisestage inglise keelse faili nimi: ")
fail_est = input("Sisestage eesti keelse faili nimi: ")

eng = open(fail_eng)
est = open(fail_est , "w")

x= eng.read()

magic = x.count("Hello")
est.write(x.replace("Hello","Tere"))


print(magic, "muudatust oli tehtud")

eng.close()
est.close()