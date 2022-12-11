eesnimi = str(input("Sisesta eesnimi: "))
perenimi = str(input("Sisesta perenimi: "))

def kasutaja(ees, pere):
    ees = ees.lower()
    pere = pere.lower()
    return ees + "." + pere

print(kasutaja(eesnimi,perenimi))