def transponeeriK(maatriks):
    maatriksT = []
    for i in range(2, -1, -1):
        el = []
        for j in range(2, -1, -1):
            el.append(maatriks[j][i])
        maatriksT.append(el)
            
    return maatriksT