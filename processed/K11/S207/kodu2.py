def transponeeriK(maatriks):
    transmaatriks = []
    for n in range(0,len(maatriks)):
        for i in range(0,len(maatriks[0])):
            transmaatriks += [[]]
            transmaatriks[i] += [maatriks[-n-1][i]]      
    return list(filter(None, transmaatriks[::-1]))           