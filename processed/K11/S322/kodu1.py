
def seosta_lapsed_ja_vanemad(isikukoodid, nimed):
    seosed = {}
    inimesed = {}
    # loo sõnastik inimestest
    # võtmeks võta isikukood, väärtuseks nimi
    with open(nimed, "r") as fail:
        for rida in fail:
            inimesed[rida.split()[0]] = " ".join(rida.split()[1:])
    # seosta lapsed ja vanemad
    # isikukoodid asenda nimedega
    with open(isikukoodid, "r") as fail:
        for rida in fail:
            if seosed.get(inimesed[rida.split()[-1]], 0) == 0:
                seosed[inimesed[rida.split()[-1]]] = set()
            seosed[inimesed[rida.split()[-1]]].add(inimesed[rida.split()[0]])
    return seosed

lapsed = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")

for key in lapsed:
    vanemad = ", ".join(list(lapsed[key]))
    print(f"{key}: {vanemad}")
