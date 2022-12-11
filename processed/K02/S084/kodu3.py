eesnimi = input("Sisesta eesnimi: ")
perenimi = input("Sisesta perenimi: ")

#paneb eesnime ja perenime vahele punkti ja teeb sellest kasutajanime
kasutajanimi = eesnimi.lower() + "." + perenimi.lower()

#muudab täpitähed ära
kasutajanimi = kasutajanimi.replace("õ","o").replace("ä","a").replace("ü","u").replace("ö","o")

print(kasutajanimi)