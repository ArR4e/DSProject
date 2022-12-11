def transponeeriK(maatriks):
    transponeeritud = {}
    for i in range(len(maatriks) - 1, -1, -1):
        for e in range(len(maatriks[i]) - 1, -1, -1):
            if e not in transponeeritud:
                transponeeritud[e] = list()
            transponeeritud[e].append(maatriks[i][e])
    maatriks_t = list()
    for el in transponeeritud:
        maatriks_t.append(transponeeritud[el])
    return maatriks_t

