
def seosta_lapsed_ja_vanemad(a , b):
    d = {}
    ikoodid = {}
    f1 = open(b)
    f2 = open(a)
    for rida in f1:
        ikoodid[rida.split(" ", 1)[0].strip()] = rida.split(" ",1)[1].strip()
    for rida in f2:
        if rida.split()[1] in ikoodid:
            vanemad = d.get(ikoodid[rida.split()[1]], set())
            vanemad.add(ikoodid[rida.split()[0]])
            d[ikoodid[rida.split()[1]]] = vanemad
    return d
        
for laps, vanem in seosta_lapsed_ja_vanemad("lapsed.txt" , "nimed.txt").items():
    print(laps + ": " +  ", ".join(list(vanem)))
