def moos(suur,väike,kogus):
    kasutatud_karpe=0
    while kogus>0 and suur>0:
        kogus-=5
        suur-=1
        kasutatud_karpe+=1
        
    if kogus>väike:
        return("-1")
    else:
        kokku_karpe=kasutatud_karpe+kogus
        return(kokku_karpe)