def moos(karp_5, karp_1, moosi_kogus, karpide_kogus = 0):
    if moosi_kogus <= 0:
        return karpide_kogus
    elif karp_1 == 0:
        return -1
    else:
        if karp_5 > 0 and moosi_kogus - 5 >= 0:
            return moos(karp_5 - 1, karp_1, moosi_kogus - 5, karpide_kogus + 1)
        else:
            return moos(karp_5, karp_1 - 1, moosi_kogus - 1, karpide_kogus + 1)

print(moos(5, 1, 9))