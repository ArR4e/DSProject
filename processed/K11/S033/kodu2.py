def transponeeriK(m):
    transponeeritud = []
    for i in range(len(m[0])-1,-1,-1):
        rida = []
        for j in range(len(m)-1,-1,-1):
            rida.append(m[j][i])
        transponeeritud.append(rida)
    return transponeeritud
