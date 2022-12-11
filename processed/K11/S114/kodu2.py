def transponeeriK(maatriks):
    
    vastus = []
    print(len(maatriks))
    for i in range((len(maatriks[0])-1),-1,-1):
        järjend1 = []
        for j in range((len(maatriks)-1),-1,-1):
            järjend1.append((maatriks[j][i]))
        vastus += [järjend1]
        #print()
    return vastus
#transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]])
