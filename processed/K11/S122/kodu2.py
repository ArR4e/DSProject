def transponeeriK(maatriks):
    tulem=[]
    rida=[[read[i] for read in maatriks] for i in range(len(maatriks[0]))]
    ridad = rida[::-1]
    for i in ridad:
        trans_read = i[::-1]
        tulem.append(trans_read)
    return (tulem)