def seosta_lapsed_ja_vanemad(lapsed,nimed):
    nimi={}
    for rida in nimed:
        rida=rida.strip().split()
        nimi[rida[0]]=rida[1]+ (" ") + rida[2]
    lõpp={}
    hulk=set()
    for rida in lapsed:
        hulk.clear()
        rida=rida.strip().split()
        if nimi[rida[1]] not in lõpp:
            lõpp[nimi[rida[1]]]=nimi[rida[0]]
        elif nimi[rida[1]] in lõpp:
            hulk.add(lõpp[nimi[rida[1]]])
            hulk.add(nimi[rida[0]])
            lõpp[nimi[rida[1]]]=hulk
        
        
#     lõpp={}
#     hulk=set()
#     for i in nimi:
#         hulk.clear()
#         if nimi[i] not in lõpp:
#             lõpp[nimi[kood[i]]]=nimi[i]
#         elif nimi[i] in lõpp:
#             try:
#                 hulk.add(lõpp[nimi[kood[i]]])
#                 hulk.add(nimi[i])
#                 lõpp[nimi[kood[i]]]=hulk
#             except KeyError:
                
    return(lõpp)
        


lapsed=open("lapsed.txt")
nimed=open("nimed.txt")
print(seosta_lapsed_ja_vanemad(lapsed,nimed))


#Loe otse "kood" failist ja hakka kohe dictionarisse lisama, kui juba on dictionarys, tee set ja lisa.