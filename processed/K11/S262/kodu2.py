def transponeeriK(maatriks):
    transponeeritud = []
    i = len(maatriks)
    k = 0
    j = len(maatriks[0])
    while k < j:
        transponeeritud.append([])
        k += 1
    for rida in maatriks:
        l = 0
        while l < j:
            transponeeritud[l].append(rida[l])
            l += 1
    return transponeeritud
