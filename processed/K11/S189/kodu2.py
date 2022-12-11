def transponeeriK(maatriks):
    järjend_kokku = []
    #elemendi valimine
    for i in range((len(maatriks[0])-1),-1,-1):
        järjend = []
        #listi valimine maatriksist
        for j in range((len(maatriks)-1),-1,-1):
            arv = maatriks[j][i]
            järjend.append(arv)
        järjend_kokku.append(järjend)
    return(järjend_kokku)

#print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
#print(transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]]))
#print(transponeeriK([[4, 31, 67, 99]]))