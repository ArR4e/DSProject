def seosta_lapsed_ja_vanemad(laste_fail, nimed):
    f1=open(laste_fail, "r", encoding="UTF-8")
    f2=open(nimed, "r", encoding="UTF-8")
    isikukoodid=[]
    sõnastik={}
    sõnastik2={}
    for rida in f2:
        rida=rida.strip()
        rida_list2=rida.split(" ")
        nimi=rida_list2[1]+' '+rida_list2[2]
        sõnastik[rida_list2[0]]=nimi
    for rida in f1:
        rida=rida.strip()
        rida_list1=rida.split(" ")
        
        if sõnastik[rida_list1[1]] not in sõnastik2:
            
            sõnastik2[sõnastik[rida_list1[1]]]={sõnastik[rida_list1[0]]}
        else:
            sõnastik2[sõnastik[rida_list1[1]]].add(sõnastik[rida_list1[0]])
    f1.close()
    f2.close()
    return sõnastik2
#         for el in sõnastik:
#             if rida_list1[1]==el:
#                 if sõnastik[el] in sõnastik2:
#                     sõnasik2[sõnastik[el]].add(rida_list2[0])
#                 else:
#                     sõnastik2[sõnastik[el]]={rida_list1[0]}
#                 
#                 isikukoodid.append(rida_list1)
#             if rida_list1[0]==el:
#                 sõnastik2[sõnastik]

#     for rida in f1:
#         rida=rida.strip()
#         rida_list1=rida.split(" ")
#         isikukoodid.append(rida_list1)
    
#     uus_sõnastik={}
#     for i in range(len(isikukoodid)):
#         uus_sõnastik[isikukoodid[i][1]]={isikukoodid[i][0]}
#     print(uus_sõnastik)
#     for el1 in uus_sõnastik:
#         for isikukood, nimi in sõnastik.items():
#             if el1==isikukood: #Kuidas asendada sõnastikus olev võti???
#                 sõnastik[nimi]=sõnastik[el1]
#                 del sõnastik[el1] # see asendus ei tee tööd!
#     print(uus_sõnastik)           
    #for el in isikukoodid
#     for isikukood, nimi in sõnastik.items():
#         for isikukood1, isikukood2 in sõnastik2.items():
#                 if isikukood==isikukood1:
#                     sõnastik3[isikukood2]=set()
#                     sõnastik3[isikukood2].add(nimi)
#     for isikukood1, isikukood2 in sõnastik2.items():
#         for isikukood, nimi in sõnastik.items():
            
    #while j<len(isikukoodid):
        
#     for i in range(len(isikukoodid)):
#         j=1
#         if isikukoodid[i][j]==
#                 
#         print(isikukood)
#         print(nimi)
#         for rida in f1:
#             rida=rida.strip()
#             rida_list1=rida.split(" ")
#         
#             if isikukood ==rida_list1[1]:
#                 rida_list1[1]=nimi
#             if isikukood ==rida_list1[0]:
#                 rida_list1[0]=nimi
#                 
#             sõnastik2[rida_list1[1]]=rida_list1[0]
#        
    
#     print(sõnastik)
#     print(sõnastik2)
laste_fail="lapsed.txt"
nimed="nimed.txt"
sõnastik2=seosta_lapsed_ja_vanemad(laste_fail, nimed)
for el in sõnastik2:
    print(str(el)+': '+str(', '.join(list(sõnastik2[el]))))
 