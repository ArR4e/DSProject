def moos(suur, väike, kogus):
    karpide_arv = 0
    while suur > 0 and 5 <= kogus:
        kogus -= 5
        suur -= 1
        karpide_arv += 1
    while väike > 0 and 1 <= kogus:
        kogus -= 1
        väike -= 1
        karpide_arv += 1
    if kogus != 0:
        return -1
    else:
        return karpide_arv
        