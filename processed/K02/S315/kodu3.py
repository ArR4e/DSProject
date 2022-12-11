ees = str(input("Ütle mulle oma ilus eesnimi: "))
pere = str(input("Ütle mulle see perenimi kah: "))

a = ees.lower()
b = pere.lower()

c = a+"."+b
#Programm muutis enne ka täpitähed väikseks, aga nüüd eemaldab eelmainitud täpid
c = c.replace("ö","o").replace("ä","a").replace("õ","o").replace("ü","u")

print(c)
