def seosta_lapsed_ja_vanemad(lapsed_fail,nimed_fail):
    sõnastik1={}
    sõnastik2={}
    nimed_fail=open(nimed_fail, "r", encoding="UTF-8")
    for rida1 in nimed_fail:
        rida1=rida1.rstrip()
        rida1.split()
        sõnastik1[rida1[0:11]]=rida1[12:]
        
    lapsed_fail=open(lapsed_fail, "r", encoding="UTF-8")
    for rida in lapsed_fail:
        rida=rida.rstrip()
        rida=rida.split(" ")
        vanem=sõnastik1[rida[0]]
        laps=sõnastik1[rida[1]]
        if laps in sõnastik2:
            sõnastik2[laps].add(vanem)
        else:
            sõnastik2[laps]=set()
            sõnastik2[laps].add(vanem)
    return sõnastik2
#         sõnastik2[nimi]=set()
#         if rida[12:] in sõnastik2:
#             sõnastik2[nimi].add(sõnastik2[sõnastik1[rida1[0:11]]])
#         print(sõnastik2)
    

seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")