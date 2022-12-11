def moos(suur,väike,kogus):

    suurte_arv= 0
    väikeste_arv= 0

    while kogus // 5 >0 : #kuni veel on võimalik suurt karpi moosikogusest lahutada
        if suur== 0: #kui karpe pole, jätab kohe vahele (null on ka täisarv, nagu ülesandes nõutud)
            break
        
        kogus= kogus-5 #lahutame suure purgi koguse
        suurte_arv+= 1
        
        if suurte_arv== suur: #kui olemas olevate kastide arv jõuab kätte, siis enam ei lahuta
            break
    while kogus // 1 >0: #kuni veel on võimalik väikseid karpe kasutada
        if väike== 0: #kui karpe pole, siis jätab vahele
            break
        
        kogus= kogus-1 #lahutame väikseid karpe
        väikeste_arv+= 1
        
        if väikeste_arv== väike: #kui väiksed kastid otsa saavad
            break

    #nüüd tuleb vaadata, kas saime moosikoguse kokku
    if kogus>0 :
        return(-1)
    else:
        return(suurte_arv+väikeste_arv)

        
    