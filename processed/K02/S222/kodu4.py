fail1 = input("Sisesta esimese faili nimi: ")
fail2 = input("Sisesta teise faili nimi: ")

if ".txt" not in fail1:
    fail1 += ".txt"
else:
    pass

if ".txt" not in fail2:
    fail2 += ".txt"
else:
    pass


failinglise = open(fail1,"r")
faileesti = open(fail2,"w")

failitekstinglise = failinglise.read()
asendused = failitekstinglise.count("Hello")
failitekstinglise = failitekstinglise.replace("Hello","Tere")

faileesti.write(failitekstinglise)
print("Tehti",asendused,"asendust")

failinglise.close()
faileesti.close()