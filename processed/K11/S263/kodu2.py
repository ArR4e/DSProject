def transponeeriK(maatriks):
    transponeeritud = []
    for i in range((len(maatriks[0]) - 1), -1, -1):
        # transponeeritud maatriksi rida
        transp_rida = []
        for j in range((len(maatriks) - 1), -1, -1):
            # muutuja - element transponeeritud maatriksi reas
            element_transp_rida = maatriks[j][i]
            transp_rida.append(element_transp_rida)
        transponeeritud.append(transp_rida)
    return transponeeritud


maatriks = [[1, 2, 3], [4, 5, 6]]

transponeeriK(maatriks)
