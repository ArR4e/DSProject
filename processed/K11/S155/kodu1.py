# #def seosta_lapsed_ja_vanemad(fail1, fail2):
#fail1 = open("lapsed.txt")
# d = {}
# e = {}
# lõpp = {}
# 
# for y in fail1:
#     rida = y.strip().split(' ')
#     d[rida[0]] = rida[1]
#     
#fail1.close()
# 
#fail2 = open("nimed.txt")
# 
# for x in fail2:
#     rida2 = x.strip().split(' ', 1)
#     e[rida2[0]] = rida2[1]
#     
#fail2.close()
# for el in 
# 
# print(e)
# print(d)

fail1 = open("lapsed.txt")
fail2 = open("nimed.txt")

def seosta_lapsed_ja_vanemad(fail1,fail2):
    lapsed = {}
    nimed = {}
    vanemad = {}
    for rida in fail1:
        a = rida.strip().split()
        if a[1] not in lapsed:
            lapsed[a[1]] = a[0]
        else:
            lapsed[a[1]]= {lapsed[a[1]], a[0]}
    for x in fail2:
        rida2 = x.strip().split(' ', 1)
        isikukood = rida2[0]
        nimi = rida2[1]
        if isikukood in lapsed.keys():
            lapsed[nimi] = lapsed.pop(isikukood)

    return lapsed
print(seosta_lapsed_ja_vanemad(fail1,fail2))

# def seosta_lapsed_ja_vanemad(fail1, fail2):
#     d = {}
#     nimed = {}
#     uuslapsed = {}
#     koodid = []
#     
#     
#     for y in fail1:
#         rida = y.strip().split(' ')
#         d[rida[0]] = rida[1]
#         koodid.append(rida[0])
#         koodid.append(rida[1])
#     for x in fail2:
#         rida2 = x.strip().split(' ',1)
#         nimed[rida2[0]] = rida2[1]
#         
#     
#     for el in koodid:
#         if el in nimed.keys():
#             index = koodid.index(el)
#             koodid[index] = nimed[el]
#             
#     i = 0
#     j = 1
#    
#     while j in range(len(koodid)):
#         for el in koodid:
#             d[koodid[0]] = koodid[1]
#             j += 1
#             i += 1
#         
#     for vanem, laps in d.items():
#         uued = uuslapsed.get(laps, set())
#         uued.add(vanem)
#         uuslapsed[laps] = uued
#                 
#     return uuslapsed
# print(seosta_lapsed_ja_vanemad(fail1,fail2))        
fail1.close()
fail2.close()