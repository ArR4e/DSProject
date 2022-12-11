e=(input("Esimese faili nimi(ilma .txt lõputa): ")+".txt")
t=(input("Teise faili nimi: ")+".txt")

eo= open(e, "r")
data=eo.read()
c= data.count("Hello") + data.count("hello")
to=open(t,"w")


to.write(eo.read().replace("Hello","Tere").replace("hello","tere"))
to.close()
eo.close()
print("Tehti " + str(c) + " asendamist")