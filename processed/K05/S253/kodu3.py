def moos(suured_karbid, väikesed_karbid, moosi_kogus):
    karpide_arv = 0
    temp_suured_karbid = suured_karbid
    temp_väikesed_karbid = väikesed_karbid
    temp_moosi_kogus = moosi_kogus

    while True:

        if(temp_suured_karbid == 0 and temp_väikesed_karbid == 0 and temp_moosi_kogus != 0)\
        or(temp_suured_karbid != 0 and temp_väikesed_karbid == 0 and temp_moosi_kogus < 5)\
        or(temp_suured_karbid == 0 and temp_väikesed_karbid != 0 and temp_moosi_kogus > temp_väikesed_karbid)\
        or(temp_suured_karbid != 0 and temp_väikesed_karbid == 0 and temp_moosi_kogus % temp_suured_karbid != 0):
            #print("Suured karbid: " + str(temp_suured_karbid))
            #print("vaikesed karbid: " + str(temp_väikesed_karbid))
            #print("moos: " + str(temp_moosi_kogus))
            return -1

        # kui saab moosi panna suurde karpi
        if temp_moosi_kogus >= 5 and temp_suured_karbid > 0:
            karpide_arv += 1
            temp_moosi_kogus -= 5
            temp_suured_karbid -= 1
            continue
            
        #kui saab moosi panna vaikesesse karpi
        if temp_väikesed_karbid > 0 and temp_moosi_kogus != 0:
            karpide_arv += 1
            temp_moosi_kogus -= 1
            temp_väikesed_karbid -= 1

            if temp_moosi_kogus == 0:
                return karpide_arv
            continue
        break
    #print("Suured karbid: " + str(temp_suured_karbid))
    #print("vaikesed karbid: " + str(temp_väikesed_karbid))
    #print("moos: " + str(temp_moosi_kogus))
    return karpide_arv