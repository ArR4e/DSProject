# 11.2. Maatriksi transponeerimine kõrvaldiagonaali järgi (kodu2)

def transponeeriK(maatriks):
    uus = []
    for rida in range(2,-1,-1):
        elemendid = []
        for j in range(1,-1,-1):
            elemendid.append(maatriks[j][rida])
        uus.append(elemendid)
    print(uus)
            
    #return maatriksT # maatriksi transponeeritud kuju kõrvaldiagonaali järgi

#print(transponeeriK([[1, 2, 3],   ## [[9, 6, 3],
                     #[4, 5, 6],   ##  [8, 5, 2],
                     #[7, 8, 9]])) ##  [7, 4, 1]]

#print(transponeeriK([[1, 2], ## [[8, 6, 4, 2],
                     #[3, 4], ##  [7, 5, 3, 1]]
                     #[5, 6], 
                     #[7, 8]]))

print(transponeeriK([[4, 31, 67, 99]]))  ## [[99], [67], [31], [4]]

