fail_lapsed=open('lapsed.txt', 'r')
fail_nimed=open('nimed.txt','r')


def seosta_lapsed_ja_vanemad(fail_lapsed, fail_nimed):
    sõnastik={}
    i=0
    lapse_isikukood=[]
    for a in fail_lapsed:
        lapsed=a.split(' ')
        lapse_isikukood.append(lapsed[0])
    
    for b in fail_nimed:
        nimed=b.split(' ')
        if nimed[0]in lapse_isikukood:
            sõnastik[nimed[1]]=set()
        if nimed[0] not in lapse_isikukood:
            
    
#     for i in fail_lapsed:
#         lapse=i.split(' ')
#         for j in fail_nimed:
#             nimed=j.split(' ')
#             if lapse[0]==nimed[0]:
#                 sõnastik[nimed[1]]=set()
#                 if lapse[1]==nimed[0]:
#                     sõnastik[nimed[1]].add(nimed[0])
                    

seosta_lapsed_ja_vanemad(fail_lapsed, fail_nimed)   
