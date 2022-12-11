en = input("Sisestage eesnimi: ")
#en = e(es)n(imi)
pn = input("Sisestage perenimi: ")
#pn = p(ere)n(imi)

En = en.replace("ä", "a").replace("õ", "o").replace("ö", "o").replace("ü", "u")
Pn = pn.replace("ä", "a").replace("õ", "o").replace("ö", "o").replace("ü", "u")
#praegune kood ei vaheta välja upper case täpitähti, selle jaoks peaksin
#lisama sama koodi aga upper case täpitahtedega
print(En.lower() + "." + Pn.lower())