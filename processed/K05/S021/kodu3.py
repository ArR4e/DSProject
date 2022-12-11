#suured karbid - 5kg
#väiksed karbid - 1kg
def moos(suuredkarbid, väikesedkarbid, moosikogus):

    karpide_kogus = 0
    while True:
        if moosikogus - 5 >= 0 and suuredkarbid > 0:
            moosikogus = moosikogus - 5
            suuredkarbid = suuredkarbid - 1
            karpide_kogus = karpide_kogus + 1
            continue
    
        if moosikogus == 0:
            return karpide_kogus
            break
        else:
            if väikesedkarbid >= moosikogus:
                karbid_kokku = karpide_kogus + moosikogus
                return karbid_kokku
                break
            else:
                return -1
                break
            
moos(1, 2, 10)
        
        
        
        
    
    
    