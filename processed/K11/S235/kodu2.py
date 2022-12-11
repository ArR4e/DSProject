def transponeeriK(maatriks):
    rida = [[read[i] for read in maatriks] for i in range(len(maatriks[0]))]
    
    read1 = rida[::-1]
    uus = []
    for i in read1:
        transponeeritud_read = i[::-1]
        uus.append(transponeeritud_read)
    return(uus)