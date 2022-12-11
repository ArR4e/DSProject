suured_karbid = int(input("Sisesta suurte karpide arv: "))
väiksed_karbid = int(input("Sisesta väikeste karpide arv: "))
kogus = int(input("Sisesta keedetava moosi kogus kilogrammides: "))

def moos(suured_karbid, väiksed_karbid, kogus) :
    n = 0
    m = 0 
    if (suured_karbid * 5 + väiksed_karbid) < kogus:
        return -1
    elif kogus < 1:
        return 0
    while suured_karbid >= 1:
        kogus = kogus - 5
        suured_karbid = suured_karbid - 1
        n = n + 1
        if kogus < 0:
            return -1
        elif kogus < 5:
            break
    while väiksed_karbid >= 1:
        kogus = kogus - 1
        väiksed_karbid = väiksed_karbid - 1
        m = m + 1
        if kogus <  1:
            break
    if kogus != 0:
        return -1
    return n + m        
print(moos(suured_karbid, väiksed_karbid, kogus))