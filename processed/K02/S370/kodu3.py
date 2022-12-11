ees=input("Mis on su eesnimi?")
taga=input("Mis on su perekonnanimi?")

nimi=ees.lower()+"."+taga.lower()
nimimod=nimi.replace("ä","a").replace("ö","o").replace("ü","u").replace("õ","o")

print(nimimod)
