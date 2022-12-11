def moos(suur_karp,väike_karp, moosi_kaal):
    suur_karp_kg=5
    väike_karp_kg=1
    antud_moosi_kaal=moosi_kaal   
    i=0
    y=0
   
    while moosi_kaal>suur_karp_kg:
        moosi_kaal=moosi_kaal-suur_karp_kg
        i=i+1
    while moosi_kaal>=väike_karp_kg:
        moosi_kaal=moosi_kaal-väike_karp_kg
        y=y+1
    vajalik_karpide_kogus=i+y
    karpidesse_läheb_teor=i*suur_karp_kg+y*väike_karp_kg
    
    moosi_kaal=antud_moosi_kaal
    karpide_kogus=suur_karp+väike_karp
    
#     while moosi_kaal>suur_karp_kg:
#         moosi_kaal=moosi_kaal-suur_karp_kg
#         i=i+1
#     while moosi_kaal>=väike_karp_kg:
#         moosi_kaal=moosi_kaal-väike_karp_kg
#         y=y+1
    if suur_karp==0 and väike_karp!=0:
        karpidesse_läheb_reaal=väike_karp_kg*väike_karp
        if moosi_kaal==karpidesse_läheb_reaal:
            u=väike_karp
        elif moosi_kaal<karpidesse_läheb_reaal:
            u=moosi_kaal
        else:
            u=-1
    elif suur_karp!=0 and väike_karp==0:
        karpidesse_läheb_reaal=suur_karp_kg*suur_karp
        if moosi_kaal==karpidesse_läheb_reaal:
            u=suur_karp
        elif moosi_kaal<karpidesse_läheb_reaal:
            v=moosi_kaal//suur_karp_kg
            if moosi_kaal % suur_karp_kg !=0:
                u=-1
            else:
                u=v
                
        else:
            u=-1
    else:
        karpidesse_läheb_reaal=suur_karp_kg*suur_karp+väike_karp_kg*väike_karp
        suuri_karpe=min(i, suur_karp)
        if y>väike_karp:
            u=-1
        elif i>suur_karp:
            u=(moosi_kaal-5*suuri_karpe)+suuri_karpe
            if moosi_kaal>karpidesse_läheb_reaal:
                u=-1
        elif moosi_kaal==karpidesse_läheb_reaal:
            u=karpide_kogus
        elif moosi_kaal<karpidesse_läheb_reaal:
            u=vajalik_karpide_kogus
        elif moosi_kaal>karpidesse_läheb_reaal:
            u=-1
        
    
    return u

suur_karp=5
väike_karp=1
moosi_kaal=9
karpide_arv=moos(int(suur_karp),int(väike_karp), int(moosi_kaal))
print(karpide_arv)
    
    