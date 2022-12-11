from math import floor

suur = int(input("Sisesta suurte karpide arv: "))
väike = int(input("Sisesta väikeste karpide arv: "))
kokku = int(input("Sisesta moosi kogus: "))



def moos(suur, väike, kokku):
    if kokku > suur * 5 + väike or kokku%5 > väike:
        return -1
    else:
        suurte_arv1 = kokku / 5
        if suur < suurte_arv1:
            suurte_arv1 = suur
        suurte_arv2 = int(suurte_arv1)
        alles = kokku - suurte_arv2 * 5
        väike_arv = alles
        return suurte_arv2 + väike_arv

print(moos(suur, väike, kokku))