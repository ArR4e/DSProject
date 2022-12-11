def seosta_lapsed_ja_vanemad(fail1, fail2):
    i= 0
    j= 0
    sõnastik = {}
    fail1 = open('nimed.txt')
    fail2 = open('lapsed.txt')
    for rida in fail1:
        Rida= rida.split(' ')
        isikukood= Rida[0]
        nimi= Rida[1:3]
        isikukood, nimi = Rida
        sõnastik[isikukood] = nimi
    for rida in fail2:
        eraldatudRida = rida.split(' ')
        vanematekood = int(eraldatudRida[0])
        lastekood = int(eraldatudRida[1])
        
            
            
        
#     i = 0
#     j= 0
#     for i in list1:
#         if list2[j] == isikukood[i]:
#             
        #1)lastekoodist leida lapsed, vanematekoodist vanemad
            #vanematekoodist on vaja leida
            
                                
                                
                        
        
    


seosta_lapsed_ja_vanemad('lapsed.txt','nimed.txt')
    