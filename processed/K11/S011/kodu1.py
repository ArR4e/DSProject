fail_1 ="lapsed.txt"
fail_2 = "nimed.txt"
def  seosta_lapsed_ja_vanemad(fail_1, fail_2):
    f = open(fail_1)
    read = f.readlines()
    f.close()
    # isikukoodide kättesaamine failist ja järjendisse panemine
    lapsed_id = []
    vanemad_id = []
    for rida in read:
        isikukoodid = (rida.strip("\n")).split(" ")
        vanemad_id.append(isikukoodid[0])
        lapsed_id.append(isikukoodid[1])
    
    # nime ja vastava id kättesaamine failist ja järjendisse panemine
    f = open(fail_2)
    nim_read = f.readlines()
    f.close()
    nimed = []
    nime_id = [] # nimele vastav id
    for rida in nim_read:
        isik_nimi = (rida.strip("\n")).split(" ")
        nimed.append(isik_nimi[1]+" "+isik_nimi[2])
        nime_id.append(isik_nimi[0])
    # lapse ja vanemate kokkuviimine
    sõnastik = {}
    for el in lapsed_id:
        lapsevanema_id = vanemad_id[lapsed_id.index(el)]
        lapse_nimi = nimed[nime_id.index(el)]
        lapsevanema_nimi = nimed[nime_id.index(lapsevanema_id)]
        if lapse_nimi not in sõnastik:
            lapsevanemate_nimed = set()
            sõnastik[lapse_nimi]= lapsevanemate_nimed
            sõnastik[lapse_nimi].add(lapsevanema_nimi)
        else:
            sõnastik[lapse_nimi].add(lapsevanema_nimi)
    return sõnastik
printimiseks = seosta_lapsed_ja_vanemad(fail_1, fail_2)
for lapse_nimi, lapsevanemate_nimed in printimiseks.items():
    print(lapse_nimi, ": ", str(lapsevanemate_nimed))

