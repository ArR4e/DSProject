a = str(input("Sisesta enda eesnimi: "))
b = str(input("Sisesta enda perekonna nimi: "))

print("Sinu kasutaja nimi on: ", a.lower().replace("ä","a").replace("ü","u")
      .replace("õ","o").replace("ö","o") + "." + b.lower().replace("ä","a")
      .replace("ü","u").replace("õ","o").replace("ö","o"))