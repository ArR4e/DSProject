def moos(suurte_karpide_arv, väikeste_karpide_arv, moosi_kogus):
    x = 0
    while suurte_karpide_arv > 0 and moosi_kogus > 5:
        moosi_kogus -= 5
        suurte_karpide_arv -= 1
        x += 1
        if moosi_kogus < 5 and moosi_kogus > 0:
            while väikeste_karpide_arv > 0 and moosi_kogus > 0:
                moosi_kogus -= 1
                väikeste_karpide_arv -= 1
                x += 1
                if moosi_kogus > 0 and väikeste_karpide_arv == 0:
                    print(-1)
                    break
        if moosi_kogus > 0 and suurte_karpide_arv == 0:
            print(-1)
            break
    if moosi_kogus == 0 and suurte_karpide_arv >= 0 and väikeste_karpide_arv >= 0:
        print(x)    

x = int(input())
y = int(input())
z = int(input())
moos(x, y, z)