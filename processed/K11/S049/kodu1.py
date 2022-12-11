fail1 = open('lapsed.txt')
fail2 = open('nimed.txt')

def seosta_lapsed_ja_vanemad(a, b):
    sõnastik = {}
    isikukoodid = {}
    nimed = {}
    for rida in fail1:
        a = rida.strip().split()
        lapse_id = a[-1]
        vanema_id = a[0]
        if lapse_id in isikukoodid:
            isikukoodid[lapse_id].add(vanema_id)
        else:
            isikukoodid[lapse_id] = {vanema_id}
        
    for rida in fail2:
        b = rida.strip().split(' ' , 1)
        nimed[b[0]] = b[1]
    
    for el in isikukoodid:
        if len(isikukoodid[el]) == 1: 
            sõnastik[nimed[el]] = {nimed[isikukoodid[el].pop()]}
        else:
            sõnastik[nimed[el]] = {nimed[isikukoodid[el].pop()], nimed[isikukoodid[el].pop()]}
    return(sõnastik)     
       
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))