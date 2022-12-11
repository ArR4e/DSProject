def moos(suured_karbid, väikesed_karbid, moosi_kogus):
    kasutatud_karbid = 0
    while suured_karbid > 0 and moosi_kogus >= 5:
        moosi_kogus -= 5
        suured_karbid -= 1
        kasutatud_karbid += 1
    while väikesed_karbid > 0 and moosi_kogus > 0:
        moosi_kogus -= 1
        väikesed_karbid -= 1
        kasutatud_karbid += 1
    if moosi_kogus == 0:
        return kasutatud_karbid
    else:
        return -1
    
suured_karbid = int(input('Sisestage suurte karpide kogus: '))
väikesed_karbid = int(input('Sisestage väikeste karpide kogus: '))
moosi_kogus = int(input('Sisestage keedetud moosi kogus: '))
    
print(moos(suured_karbid, väikesed_karbid, moosi_kogus))