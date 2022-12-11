def transponeeriK(maatriks):
    vastus=[]
    for i in range(len(maatriks[0]),0,-1):
        t=[]
        for j in range(len(maatriks),0,-1):
            t.append(maatriks[j-1][i-1])
        vastus.append(t)
    return vastus

        