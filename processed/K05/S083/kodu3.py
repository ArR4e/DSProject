def moos(s,v,keedumoos):
    n=0
    while keedumoos >=5 and s>0:
        keedumoos = keedumoos-5
        s = s - 1
        n=n+1
    while v > 0 and keedumoos > 0:
        keedumoos = keedumoos-1
        v = v - 1
        n=n+1
    if keedumoos == 0:
        return n
    else:
        return -1
    
suured_karbid=int(input('Sisesta suurte karpide arv: '))
väikesed_karbid=int(input('Sisesta väikeste karpide arv: '))
keedumoos=int(input('Sisesta moosi kogus kilogrammides: '))



print(moos(suured_karbid,väikesed_karbid,keedumoos))