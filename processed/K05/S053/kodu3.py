def moos(suured_karbid, väikesed_karbid, moosi_kogus):
    suuri_karpe_vaja = moosi_kogus // suured_karbid
    suuri_karpe_on = min(suuri_karpe_vaja, suured_karbid)
    väikeseid_karpe_vaja = (moosi_kogus - (suuri_karpe_on*5))
    
    while väikeseid_karpe_vaja <= väikesed_karbid:
        karbid = suuri_karpe_on +väikeseid_karpe_vaja
        return karbid
    else: 
        return -1
    
    
    