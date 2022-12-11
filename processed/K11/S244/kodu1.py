def seosta_lapsed_ja_vanemad(fail1,fail2):
    sõnastik = {}
    faili_sisu1 = []
    faili_sisu2 = []
    for x in fail1:
        faili_sisu1.append(x.strip())
    for x in fail2:
        faili_sisu2.append(x.strip())
        
    for rida1 in faili_sisu1:
        for rida2 in faili_sisu2:
            järjend1 = rida1.strip().split(" ")
            järjend2 = rida2.strip().split(" ")
            if järjend1[1] == järjend2[0]:
                sõnastik[järjend2[1]+ " " + järjend2[2]] = set()
                
    for rida1 in faili_sisu1:
        for rida2 in faili_sisu2:
            järjend1 = rida1.strip().split(" ")
            järjend2 = rida2.strip().split(" ")   
            if järjend1[0] == järjend2[0]:
                for x in faili_sisu2:
                    järjend3 = x.strip().split(" ")
                    if järjend1[1] == järjend3[0]:
                        lisa = järjend2[1]+ " "  + järjend2[2]
                        sõnastik[järjend3[1] + " " + järjend3[2]].add(lisa)
                        
    return sõnastik
                    
    
                        
                
    
                
            

fail1 = open('lapsed.txt', encoding = 'UTF-8')
fail2 = open('nimed.txt', encoding ='UTF-8')
sõnastik = seosta_lapsed_ja_vanemad(fail1,fail2)
c = []
for võti, väärtus in list(sõnastik.items()):
    for nimi in väärtus:
        c.append(nimi)
    a = ', '.join(c)
    print(võti + ': ' + a)
    c = []