eesnimi = input("Eesnimi: ")
perenimi = input("Perenimi: ")

eesnimi_uus = eesnimi.replace("õ","o").replace("ü","u").replace("ö","o").replace("ä","a")
perenimi_uus = perenimi.replace("õ","o").replace("ü","u").replace("ö","o").replace("ä","a")

print(eesnimi_uus.lower()+"."+perenimi_uus.lower())

