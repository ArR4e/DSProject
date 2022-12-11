#transp = maatriks.transpose()
#[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
# n = len(maatriks[0])
#     L = sum(maatriks, [])
#     return [L[i::n] for i in range(n)]


# tulemus = [[[maatriks[j][i] for j in range(len(maatriks))] for i in range (len(maatriks[0]))]]
#     for row in tulemus:
#         print(row)



def transponeeriK (maatriks):
    maatriks_tulemus = []
    a = len(maatriks[0])
    for el in maatriks:
        if a!= len(el):
            print("Error.")
            return
    for i in range(len(maatriks[0])):
        rida =[]
        for j in range(len(maatriks)):
            rida.append(maatriks[j][i])
        rida2 = rida[::-1]
        maatriks_tulemus.append(rida2)
    return maatriks_tulemus[::-1]

# maatriks = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
# trym = transponeeriK (maatriks)
# print(trym)
        
    
    
        
        

        
    
        
    
    
    
    