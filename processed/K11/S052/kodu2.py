uusmaatriks = []

def transponeeriK(maatriks):
    temp = []
    i = 0
    if len(maatriks) == 1:
        for element in maatriks[0]:
            uusmaatriks.append(element)
        uusmaatriks.reverse()
        print(uusmaatriks)
    else:
        while i < len(maatriks[0]):
            for rida in maatriks:
                temp.append(rida[len(rida)-(i+1)])
            temp.reverse()
            uusmaatriks.append(temp)
            temp = []
            i+=1
    return uusmaatriks

