def seosta_lapsed_ja_vanemad(lastefail1, nimedefail1):
    sõnastik1 = {}
    sõnastik2 = {}
    lastefail = open(lastefail1)
    nimedefail = open(nimedefail1)
    for rida in lastefail:
        u_rida = rida.split(' ')
        vanema_id = u_rida[0].strip()
        lapse_id1 = u_rida[1].strip()
        if lapse_id1 in sõnastik1:
            sõnastik1[lapse_id1].add(vanema_id)
        else:
            sõnastik1[lapse_id1] = set()
            sõnastik1[lapse_id1].add(vanema_id)

    for rida2 in nimedefail:
        u_rida2 = rida2.split(' ', 1)
        vanema_nimi = u_rida2[1].strip()
        lapse_id2 = u_rida2[0].strip()
        sõnastik2[lapse_id2] = vanema_nimi
        
    sõnastik = {}
    for lapsenimi, vanemanimi in sõnastik1.items():
        laps = sõnastik2.get(lapsenimi)
        sõnastik[laps] = set()
        for element in vanemanimi:
            if element in sõnastik2:
                vanem = sõnastik2.get(element)
                sõnastik[laps].add(vanem)
            else:
                vanem = 'tühjus'
                sõnastik[laps].add(vanem)
            
    return(sõnastik)
   
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))