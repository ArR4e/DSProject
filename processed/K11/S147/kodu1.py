def seosta_lapsed_ja_vanemad(lastefail,nimefail):
    with open(lastefail) as lapsed: lapsedtekst = lapsed.read().strip().split("\n")
    with open(nimefail) as nimed: nimedtekst = nimed.read().strip().split("\n")  
    nimed = {i.split()[0]:" ".join(i.split()[1:]) for i in nimedtekst}
    nimekiri = {}
    for i in lapsedtekst:
        i = [nimed[i.split()[0]],nimed[i.split()[1]]] #asendab isikukoodid nimedega
        if i[1] in nimekiri: nimekiri[i[1]].add(i[0])
        else: nimekiri[i[1]] = {i[0]}
    return nimekiri
tulemus = seosta_lapsed_ja_vanemad(input("Sisestage laste faili nimi: "),input("Sisestage nimede faili nimi: "))
for laps,vanemad in tulemus.items(): print(f"{laps}: {', '.join(vanemad)}")