
def moos(s, v, k):
    karpide_arv = 0
    if k == 0:
        karpide_arv = 0 
    elif (s * 5) + v * 1 < k:
        karpide_arv = -1
    elif k - s <= 5 and 5 + v < k:
        karpide_arv = -1
    elif s * 5 == k:
        karpide_arv = s
    else:
        if k - (s * 5) >= 0:
            k - (s * 5)
            karpide_arv += s
            n = k - (s * 5)
            n * 1
            karpide_arv += n
        else:
            if s * 5 > k and k - s <= 5:
                karpide_arv += 1
                n = k - 5
                n * 1
                karpide_arv += n
    return karpide_arv
