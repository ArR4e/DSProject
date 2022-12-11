def moos(suur_karp, väike_karp, moosi_kogus):
    karpe_kokku = 0
    while moosi_kogus >= 5 and suur_karp > 0:
        suur_karp -= 1
        moosi_kogus -= 5
        karpe_kokku += 1
    while moosi_kogus >= 1 and väike_karp > 0:
        väike_karp -= 1
        moosi_kogus -= 1
        karpe_kokku += 1
    if moosi_kogus > 0:
        return -1
    return karpe_kokku