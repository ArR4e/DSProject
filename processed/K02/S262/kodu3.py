eesnimi = input("Sisesta eesnimi: ")
perenimi = input("Sisesta perenimi: ")
eesnimi = eesnimi.lower()
eesnimi = eesnimi.replace("õ","o")
eesnimi = eesnimi.replace("ä","a")
eesnimi = eesnimi.replace("ö","o")
eesnimi = eesnimi.replace("ü","u")
perenimi = perenimi.lower()
perenimi = perenimi.replace("õ","o")
perenimi = perenimi.replace("ä","a")
perenimi = perenimi.replace("ö","o")
perenimi = perenimi.replace("ü","u")

print(eesnimi + "." + perenimi)