
def poisse_ja_tüdrukuid(nimedelist):
    poistearv = 0
    tüdrukutearv = 0
    for x in nimedelist:
        y = x.split(" ")
        if "P" in y:
            poistearv += 1
        elif "T" in y:
            tüdrukutearv += 1
    return (poistearv, tüdrukutearv)
nimed =["Mari T", "Kadri T", "Toomas P", "Martin P", "Tiina T"]
poisse_ja_tüdrukuid(nimed)