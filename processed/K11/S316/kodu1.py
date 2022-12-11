def seosta_lapsed_ja_vanemad(lapsed,nimed):
    nimede_hulk = {}
    lapsed_ja_vanemad = {}
    for rida in nimed:
        nimi = rida.strip().split(" ",1)
        nimede_hulk[nimi[0]] = nimi[1]
    nimed.close()
    for rida in lapsed:
        isikukoodid = rida.strip().split(" ")
        if nimede_hulk[isikukoodid[1]] in lapsed_ja_vanemad:
            lapsed_ja_vanemad[nimede_hulk[isikukoodid[1]]].add(nimede_hulk[isikukoodid[0]])
        else:
            lapsed_ja_vanemad[nimede_hulk[isikukoodid[1]]] = set()
            lapsed_ja_vanemad[nimede_hulk[isikukoodid[1]]].add(nimede_hulk[isikukoodid[0]])
    lapsed.close()
    return lapsed_ja_vanemad
            

lapsed = open('lapsed.txt')
nimed = open('nimed.txt')
print(seosta_lapsed_ja_vanemad(lapsed,nimed))