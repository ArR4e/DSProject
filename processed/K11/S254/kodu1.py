def seosta_lapsed_ja_vanemad(laste_fail,nimede_fail):
    sõnastik={}
    nimede_sõnastik={}
    laste_list=[]
    vanemate_list=[]
    ik = open(laste_fail,encoding='UTF-8')
    nimed = open(nimede_fail,encoding='UTF-8')
    for rida in nimed:
        rida = rida.strip().split(' ',1)
        nimede_sõnastik[rida[0]] = rida[1]
    for rida in ik:
        rida = rida.split()
        lapse_id=rida[1]
        vanema_id=rida[0]
        if nimede_sõnastik[lapse_id] in sõnastik:
            sõnastik[nimede_sõnastik[lapse_id]].add(nimede_sõnastik[vanema_id])
        else:
            sõnastik[nimede_sõnastik[lapse_id]] = set()
            sõnastik[nimede_sõnastik[lapse_id]].add(nimede_sõnastik[vanema_id])
    return sõnastik




print(seosta_lapsed_ja_vanemad('lapsed.txt','nimed.txt'))