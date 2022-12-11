
def transponeeriK(maatriks):
    vastus_maatriks = []
    for i in range(len(maatriks[0])-1,-1,-1):
        rida = []
        for j in range(len(maatriks)-1,-1,-1):
            rida.append(maatriks[j][i])
        vastus_maatriks.append(rida)
    return vastus_maatriks


