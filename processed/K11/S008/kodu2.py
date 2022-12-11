def transponeeriK(maatriks):
    keeratudM = []
   # keeratudI = 0
    for read in range( len(maatriks)-1,-1,-1):
        keeratudI = 0
        for veerud in range(len(maatriks[0])-1,-1,-1):
            if read == len(maatriks)-1:
                keeratudM_rida = []
                keeratudM_rida.append(maatriks[read][veerud])
                keeratudM.append(keeratudM_rida)
            else:
                keeratudM[keeratudI].append(maatriks[read][veerud])
                keeratudI = keeratudI + 1
    return keeratudM
     

print(transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]]))