def seosta_lapsed_ja_vanemad(lastefail,nimedefail):
    lapsed = {}
    f = open(lastefail)
    g = open(nimedefail)
    nimedefaili_sisu = {}
    lastefaili_sisu = []
    for rida in g:
        nimi_ja_kood = rida.strip().split(" ",1)
        nimedefaili_sisu[nimi_ja_kood[0]] = nimedefaili_sisu.get(nimi_ja_kood[0],nimi_ja_kood[1])
    for rida in f:
        lastefaili_sisu +=[rida.strip().split(" ")]
    for i in range(len(lastefaili_sisu)):
        nimi = nimedefaili_sisu[lastefaili_sisu[i][1]]
        vanema_nimi = nimedefaili_sisu[lastefaili_sisu[i][0]]
        if nimi not in lapsed:
            lapsed[nimi] = set()
        lapsed[nimi].add(vanema_nimi)
    return lapsed

tulemus=seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")
for võti in tulemus:
    if len(tulemus[võti]) == 2:
        print(võti+": "+', '.join(tulemus[võti]))
    else:
        print(võti+": "+''.join(tulemus[võti]))