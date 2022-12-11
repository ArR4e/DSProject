def transponeeriK(maatriks):
    vastus = []
    for j in range(len(maatriks[0])-1, -1, -1):
        rida = []
        for i in range(len(maatriks)-1, -1, -1):
            rida.append(maatriks[i][j])
        vastus.append(rida)
    return vastus