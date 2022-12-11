def transponeeriK(maatriks):
    transponeeritud = []
    for j in range(len(maatriks[0])):
        mini_transponeering = []
        for i in range(len(maatriks)):
            mini_transponeering.append(maatriks[len(maatriks) - 1 - i][len(maatriks[0]) - j - 1])
        transponeeritud.append(mini_transponeering)
        
    return(transponeeritud)