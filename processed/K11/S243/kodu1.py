#1. Lapsed ja vanemad

def seosta_lapsed_ja_vanemad(lapsed, nimed):
    f=open(lapsed)
    sõnaraamat=dict()
    for rida_f in f:
        isikukoodid=rida_f.strip().split()
        g=open(nimed)
        for rida_g in g:
            nimi=rida_g.strip().split()
            isikukood=nimi[0]
            del nimi[0]
            ees_ja_perenimi=" ".join(nimi)
            if isikukood==isikukoodid[0]:
                lapsevanem=ees_ja_perenimi
            elif isikukood==isikukoodid[1]:
                laps=ees_ja_perenimi
        if laps in sõnaraamat:
            vanemad=sõnaraamat[laps]
            vanemad.add(lapsevanem)
            sõnaraamat[laps]=vanemad
        else:
            sõnaraamat[laps]={lapsevanem}
        g.close()
    f.close()
    return sõnaraamat

print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))
