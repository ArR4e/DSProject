def moos(suurte_karpide_arv, väikeste_karpide_arv, moosi_kogus):
    suured_karbid=0
    väiksed_karbid=0
    while suurte_karpide_arv > 0 and moosi_kogus >= 5:
        moosi_kogus -= 5
        suured_karbid += 1
        suurte_karpide_arv -= 1

    while väikeste_karpide_arv > 0 and moosi_kogus > 0:
        moosi_kogus -= 1
        väiksed_karbid +=1
        väikeste_karpide_arv -= 1
    if moosi_kogus == 0:
        kasutatud_karbid = väiksed_karbid + suured_karbid
    else:
        kasutatud_karbid = -1

    return (kasutatud_karbid)

suurte_karpide_arv = int(input('Sisestage suurte karpide arv: '))
väikeste_karpide_arv = int(input('Sisestage väikeste karpide arv: '))
moosi_kogus = int(input('Sisestage moosi kogus: '))

print(moos(suurte_karpide_arv, väikeste_karpide_arv, moosi_kogus))