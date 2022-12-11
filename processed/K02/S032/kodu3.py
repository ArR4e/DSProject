eesnimi = input("Eesnimi: ")
perenimi = input("Perenimi: ")
nimi = eesnimi +"." + perenimi
#https://stackoverflow.com/questions/3411771/best-way-to-replace-multiple-characters-in-a-string
kasutaja = nimi.lower().replace("õ","o").replace("ä","a").replace("ö","o").replace("ü","u")
print(kasutaja)