def moos(suured_karbid, väiksed_karbid, moosi_kogus):
    kasutatud_suured_karbid = 0
    kasutatud_väiksed_karbid = 0
    while True:
        if moosi_kogus / 5 >= 1 and suured_karbid != 0:
            suured_karbid = suured_karbid - 1
            kasutatud_suured_karbid = kasutatud_suured_karbid + 1
            moosi_kogus = moosi_kogus - 5
        elif moosi_kogus / 1 >= 1 and väiksed_karbid != 0:
            väiksed_karbid = väiksed_karbid - 1
            kasutatud_väiksed_karbid = kasutatud_väiksed_karbid + 1
            moosi_kogus = moosi_kogus - 1
        elif väiksed_karbid == 0 and moosi_kogus > 0:
            return -1
            break
        else:
            break
        
    if moosi_kogus == 0:
        karbid = kasutatud_suured_karbid + kasutatud_väiksed_karbid
        return karbid

sisestatud_suured_karbid = int(input("Sisesta suurte karpide arv: "))
sisestatud_väiksed_karbid = int(input("Sisesta väikeste karpide arv: "))
sisestatud_moosi_kogus = int(input("Sisesta moosi kogus kilogrammides: "))
print(moos(sisestatud_suured_karbid, sisestatud_väiksed_karbid, sisestatud_moosi_kogus))