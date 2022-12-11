ees1 = (str(input("Sisestage oma eesnimi: ")))
pere = (str(input("Sisestage oma perenimi: ")))
ees2 = ees1 + "."

ees3 = str.lower(ees2)
pere2 = str.lower(pere)
kassu = ees3+pere2

print(f"Teie kasutajanimi on: {kassu}")