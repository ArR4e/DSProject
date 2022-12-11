a = input("Palun sisestage oma eesnimi: ")
b = input("Palun sisestage oma perekonnanimi: ")
'''
print("Teie kasutajanimi on:", str.lower(a) + "." + str.lower(b))
'''
print("Teie kasutajanimi on:", (a.lower() + "." + b.lower()).replace("ö", "o").replace("ä", "a").replace("õ", "o").replace("ü", "u"))
'''
print("Teie kasutajanimi on:", a.casefold() + "." + b.casefold())
'''