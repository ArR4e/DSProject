def moos(suured, väiksed, moos):
    karbid = 0                           #kasutatud karpide arv kokku 
    
    while True:
        if moos >= 5 and suured >= 1:    #kontrollin kas on alles suuri karpe ja 5 kg moosi
            karbid += 1
            moos -= 5
            suured -= 1
            continue
        elif moos >= 1 and väiksed >= 1: #kontrollin kas on alles väikseid karpe ja 1 kg moosi
            karbid += 1
            moos -= 1
            väiksed -= 1
            continue
        else: 
            if moos > 0:                 #kui moosi jääb alles siis -> -1
                return -1
            else:
                return karbid            #kui moosi ei jäänud alles, tagastab karpide arvu 

print(moos(2, 6, 14))