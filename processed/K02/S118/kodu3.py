#sisend
eesnimi = input("Sisesta eesnimi: ")
perenimi = input("Sisesta perenimi: ")
#tähed tehakse läbivalt väikesteks, uue muutuja tähti hakatakse for tsüklis ükshaaval muutma täpituteks
kombinatsioon = eesnimi.lower() + "." + perenimi.lower()

väljund = ""

for täht in kombinatsioon:
    #kui tähed on nö. filtri läbinud, liidetakse need veel uude muutujasse
    if täht == "ö" or täht == "õ":
        väljund+="o"
    elif täht == "ü":
        väljund+="u"
    elif täht == "ä":
        väljund+="a"
    else:
        väljund+=täht

#programm väljastab vastuse
print(väljund)