suured = int(input("Suurte karpide arv: "))
väikesed = int(input("Väikeste karpide arv: "))
kogus = int(input("Moosi kogus: "))

def moos(suured, väikesed, kogus):
    karbid = 0
    if kogus > (suured*5 + väikesed*1):
        return -1
    elif kogus == 0:
        return 0
    elif väikesed == 0 and kogus != suured*5:
        return -1
    elif suured == 0 and väikesed >= kogus:
        karbid = kogus
        return karbid
    else:
        while kogus >= 5 and suured > 0:
            kogus -= 5
            suured -= 1
            karbid += 1
            if kogus < 5 or suured <= 0:
                if väikesed >= kogus and kogus != 0:
                    karbid += kogus
                    return karbid
                elif kogus == 0:
                    return karbid
                else:
                    return -1
    
print(moos(suured, väikesed, kogus))