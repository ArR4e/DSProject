#nädal 11, kodu 2 - maatriksi transponeerimine kõrvaldiagonaali järgi

def transponeeriK(maatriks):
    read = len(maatriks)
    kolonnid = len(maatriks[0])
    uus_maatriks=[]
    for i in range(kolonnid):
        järj = []
        for j in range(read):
            rida = read - j
            kolonn = kolonnid - i
            väärtus = maatriks[rida-1][kolonn-1]
            järj.append(väärtus)
        uus_maatriks.append(järj)
    return uus_maatriks


