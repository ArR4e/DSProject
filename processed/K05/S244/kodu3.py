def moos(Skarbid, Vkarbid, moosi_kogus):
    karpe_kokku = 0
    while moosi_kogus > 0:
        if moosi_kogus >= 5 and Skarbid > 0:
            Skarbid -= 1
            moosi_kogus -= 5
        elif Vkarbid > 0:
            Vkarbid -= 1
            moosi_kogus -= 1
        else:
            return -1
        karpe_kokku += 1
    return karpe_kokku
            
            
Skarbid = int(input("Sisesta suurte karpide arv: "))
Vkarbid = int(input("Sisesta väikeste karpide arv: "))
moosi_kogus = int(input("Sisesta keedetava moosi kogus kilogrammides: "))
print(moos(Skarbid, Vkarbid, moosi_kogus))