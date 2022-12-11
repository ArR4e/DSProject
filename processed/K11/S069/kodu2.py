def transponeeriK(maatriks):
    array = []
    for el in maatriks:
        for i in el:
            array += [i]
    vastus = []
    for n in range(int(len(array)/len(maatriks))):
        a=array[n::len(maatriks)]
        a.reverse()
        vastus+=[a]
    vastus.reverse()
    return vastus

