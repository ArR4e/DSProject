#Moosi keetmine
def moos(sk_arv, vk_arv, kogus):
    karpide_arv = 0
    karpide_mahutavus = sk_arv*5 + vk_arv
    if karpide_mahutavus < kogus:
        return -1
    else:
        for i in range(sk_arv):
            if kogus < 5:
                break
            kogus -= 5
            karpide_arv +=1
        if kogus > 0:
            for i in range(vk_arv):
                kogus -= 1
                karpide_arv +=1
                if kogus == 0:
                    break
    if kogus != 0:
        return -1
    return karpide_arv

suured_karbid = int(input("Sisesta suurte karpide arv: "))
väikesed_karbid = int(input("Sisesta väikeste karpide arv: "))
moosi_kogus = int(input("Sisesta keedetava moosi kogus kilogrammides: "))
print(moos(suured_karbid, väikesed_karbid, moosi_kogus))