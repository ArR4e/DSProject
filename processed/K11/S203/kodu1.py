def seosta_lapsed_ja_vanemad(lapse_fail, vanema_fail):
    sõnastik_vf = {}
    lõplik_s = {}
    lapse_f = open(lapse_fail, 'r', encoding='utf-8')
    vanema_f = open(vanema_fail, 'r', encoding='utf-8')
    for rida in vanema_f:
        sisu = rida.strip().split(' ')
        isikukood_vf = sisu[0]
        inimene_vf = sisu[1] +  ' ' + sisu[2]
        sõnastik_vf[isikukood_vf] = inimene_vf
    vanema_f.close()
    for rida in lapse_f:
        sisu = rida.strip().split(' ')
        lapse_ik = sisu[1]
        vanema_ik = sisu[0]
        lapse_nimi = sõnastik_vf[sisu[1]]
        vanema_nimi = sõnastik_vf[sisu[0]]
        if lapse_nimi not in lõplik_s:
            lõplik_s[lapse_nimi] = set()
        lõplik_s[lapse_nimi].add(vanema_nimi)
    lapse_f.close()
    return lõplik_s

seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for el in seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt").keys():
    v_nimed = ''
    vanemad = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")[el]
    for vanem in vanemad:
        v_nimed += vanem + ', '
    print(el+':'+ v_nimed)