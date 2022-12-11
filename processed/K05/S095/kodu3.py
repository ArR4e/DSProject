suur_karp=int(input("Sisesta suurte karpide kogus: "))
väike_karp=int(input("Sisesta väikeste karpide kogus: "))
moosi_kogus=int(input("Sisesta moosi kogus(kg): "))
def moos(suur_karp, väike_karp, moosi_kogus):
    anumate_maht=(suur_karp*5)+(väike_karp*1)
    moosi_purki=0
    if moosi_kogus>anumate_maht:
        print("-1")
    else:
        for moos_purki in range(moosi_kogus):
            if moosi_kogus>=5:
                moosi_kogus=moosi_kogus-5
                moosi_purki=moosi_purki+1
            if moosi_kogus<5 and moosi_kogus!=0:
                moosi_kogus=moosi_kogus-1
                moosi_purki=moosi_purki+1
        print(moosi_purki)
moos(suur_karp, väike_karp, moosi_kogus)       
