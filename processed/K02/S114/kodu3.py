eesnimi = str(input("Sisesta eesnimi: "))
perenimi = str(input("Sisesta perenimi: "))

uusees = eesnimi.lower().replace("ö","o").replace("õ","o").replace("ä","a").replace("ü","u")
uuspere = perenimi.lower().replace("ö","o").replace("õ","o").replace("ä","a").replace("ü","u")
print(uusees +"."+uuspere)