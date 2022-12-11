def seosta_lapsed_ja_vanemad(fail1, fail2):
    isikukoodid = []
    nimed = []
    vanemadjalapsed = {}
    
    f1 = open(fail1, encoding = 'UTF-8')
    
    for rida in f1:
        rida = rida.strip().split()
        isikukoodid.append(rida)
        
    f1.close()
    
    f2 = open(fail2, encoding = 'UTF-8')
    
    for rida in f2:
        rida = rida.strip().split(' ', 1)
        nimed.append(rida)
        
    f2.close()
    
    for i in range(len(isikukoodid)):
        laps = 0
        vanemad = set()
        for j in range(len(nimed)):
            if isikukoodid[i][1] == nimed[j][0]:
                laps = nimed[j][1]
                for n in range(len(isikukoodid)):
                    if isikukoodid[i][1] == isikukoodid[n][1]:
                        for l in range(len(nimed)):
                            if isikukoodid[n][0] == nimed[l][0]:
                                vanemad.add(nimed[l][1])
                                
                                vanemadjalapsed[laps] = vanemad
            
                        
    return vanemadjalapsed
    
lapsed = 'lapsed.txt'
nimed = 'nimed.txt'

sonastik = seosta_lapsed_ja_vanemad(lapsed, nimed)

for el in sonastik:
    vanematelist = list(sonastik[el])
    if len(vanematelist) == 2:
        print(f'{el}: {vanematelist[0]}, {vanematelist[1]}')
    else:
        print(f'{el}: {vanematelist[0]}')

        

    