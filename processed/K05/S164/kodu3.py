suuredKarbid = int(input("Suurte karpide arv: "))
väiksedKarbid = int(input("Väikeste karpide arv: "))
keedetava_moosi_kogus = int(input("Moosi kogus: "))


    
def moos(suuredKarbid, väiksedKarbid, moosi_kokku):
    max_moosikogus = suuredKarbid * 5 + väiksedKarbid
    
    if max_moosikogus < moosi_kokku:
        return -1
    
    suuri_kasutatud_karpe = 0
    while suuri_kasutatud_karpe <= suuredKarbid:
       if moosi_kokku -5 < 0:
           break
       suuri_kasutatud_karpe += 1
       moosi_kokku = moosi_kokku - 5
       
    
       
    väikseid_kasutatud_karpe = 0
    while väikseid_kasutatud_karpe <= väiksedKarbid:
        if moosi_kokku - 1 < 0:
            break
        
        väikseid_kasutatud_karpe += 1
        moosi_kokku = moosi_kokku - 1
        
    if (moosi_kokku != 0):
        return -1
        
    karpe_kokku = väikseid_kasutatud_karpe + suuri_kasutatud_karpe
    return karpe_kokku
       

karpide_arv = moos(suuredKarbid, väiksedKarbid, keedetava_moosi_kogus)
print(karpide_arv)