'''-- Kodutöö nr. 11 - 2. Maatriksi transponeerimine kõrvaldiagonaali järgi --'''
# funktsioon 'transponeeriK' võtab argumendina ette maatriksi ning
# tagastab selle transponeeritud kuju kõrvaldiagonaali järgi
##################################################################
def transponeeriK(K):
    # maatriksi transponeeritud kuju
    tr_K = []
    
    for j in range(len(K[0])-1, -1, -1):
        tr_K_rida = []
        tr_K.append(tr_K_rida)
        for i in range(len(K)-1, -1, -1):
            tr_K_rida.append(K[i][j])
    
    return tr_K
##################################################################
print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(transponeeriK([[4, 31, 67, 99]]))