suur_k = int(input("Sisestage suurte karpide arv: "))
väike_k = int(input("Sisestage väikeste karpide arv: "))
kogus = int(input("Sisestage moosi kogus (kilogrammides): "))

def moos(suur_k, väike_k, kogus):
    karpide_maht = (suur_k * 5) + (väike_k * 1)
    #kui moosi ei ole, ei saa seda karpidesse mahutada
    if kogus == 0:
        return 0
    #kui moosi tuleks liiga palju, siis Emma ei keeda moosi
    elif karpide_maht < kogus:
        return -1
    #kui moos ei mahu täspelt ära, siis Emma ei keeda moosi
    elif (suur_k * 5) / kogus != (suur_k * 5) // kogus and väike_k < kogus % 5:
        return -1
    #kui pole suuri karpe, peab mahutama väikestesse
    elif suur_k == 0:
        vaja_väikeseid = väike_k - (väike_k - kogus)
        return vaja_väikeseid
    #kui pole väikeseid karpe, peab mahutama suurtesse
    elif väike_k == 0:
        vaja_suuri = kogus // (suur_k * 5)
        return vaja_suuri
    #palju läheb karpe vaja
    else:
        vaja_suuri = 0
        while vaja_suuri < suur_k and kogus > 5:
            vaja_suuri += 1
            kogus -= 5
            
        vaja_väikeseid = 0
        while vaja_väikeseid < väike_k and kogus > 0:
            kogus -= 1
            vaja_väikeseid += 1
            
        kokku = vaja_väikeseid + vaja_suuri
        return kokku
        
print(moos(suur_k, väike_k, kogus))