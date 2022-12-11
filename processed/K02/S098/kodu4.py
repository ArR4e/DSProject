fail1 = input("sisesta esimese faili nimi: ")
f = open(fail1)
faili_sisu = f.read()
d3=faili_sisu.count("Hello")
fail2 = input("sisesta teise faili nimi: ")
g = open(fail2, "w")
d = g.write(faili_sisu.replace("Hello","Tere"))
f.close()
g.close()
print ("Tehti" + " " + str( d3) + " "+ "asendamist." )


