def seosta_lapsed_ja_vanemad(f1, f2):
    f1=open("lapsed.txt", encoding="utf-8")
    f2=open("nimed.txt", encoding="utf-8")
    nimed={}
    lapsed={}
    for rida in f1:
        ik_vanem, ik_laps = rida.strip().split(" ")
        lapsed[ik_laps]=ik_vanem
    for rida in f2:
        ik, nimi = rida.strip().split(" ", 1)
        nimed[ik]=nimi
    f1.close()
    f2.close()

    sõnastik={}
    for ik in nimed:
#         lapse_ik=lapsed[ik_laps]
#         vanema_ik=lapsed[ik_vanem]
        lapse_nimi=nimed[ik_laps]
        vanema_nimi=nimed[ik_vanem]
        sõnastik[lapse_nimi]=vanema_nimi
    return(sõnastik)
    
