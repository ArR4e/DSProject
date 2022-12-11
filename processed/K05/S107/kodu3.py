suured_karbid = int(input("Sisesta suurte karpide arv: "))
väiksed_karbid = int(input("Sisesta väikeste karpide arv: "))
kogus = int(input("Sisesta moosi kogus: "))
def moos(suured_karbid, väikesed_karbid, kogus):
    karbid = 0
    #mitu suurt karpi saaks täita
    suuri_saaks = kogus // 5
    #on nii palju s.karpe?
    if suuri_saaks > suured_karbid:
        #kui ei, kasutame kõik ära, mis olemas
        karbid = suured_karbid
    else:
        #kui on, kasutame neid maksimaalse arvu
        karbid = suuri_saaks
    #kui suur kogus jääb peale suurte täitmist üle, see on ka väikeste karpide arv
    väikeseid_vaja = kogus - 5 * karbid
    
    #kui väikeseid pole piisavalt ja moos ei mahu ära
    if väikeseid_vaja > väikesed_karbid:
        return -1
    #karpide arv kokku
    return karbid + väikeseid_vaja
print(moos(suured_karbid, väiksed_karbid, kogus))
        
        
            
            
        