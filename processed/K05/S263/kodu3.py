#suur karp = 5g
#väike karp = 1g

#suurte_karpide_arv = int(input("Sisesta suurte karpide arv: "))
#väikeste_karpide_arv = int(input("Sisesta väikeste karpide arv: "))
#moosi_kogus = int(input("Sisesta keedetava moosi kogus kg: "))

def moos(suurte_karpide_arv, väikeste_karpide_arv, moosi_kogus):
    karbid_kokku = 0
    while moosi_kogus > 0:
        while suurte_karpide_arv > 0 and moosi_kogus >= 5:
            suurte_karpide_arv -= 1
            moosi_kogus -= 5
            karbid_kokku += 1
            
        while väikeste_karpide_arv > 0 and moosi_kogus > 0:
            väikeste_karpide_arv -= 1
            moosi_kogus -= 1
            karbid_kokku += 1
    
        if moosi_kogus > 0:
            karbid_kokku = -1
            break
    
    return karbid_kokku
        

            
    
    
    
    
    