maatriks =[[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
uus_maatriks = []
def transponeeriK(maatriks, uus_maatriks):
    for i in range(len(maatriks[0])):
       # uus_maatriks = []
        rida =[]
        for asi in maatriks:
            rida.append(asi[i])
        uus_maatriks.append(rida[i])
    print(uus_maatriks)
            
        
        
transponeeriK(maatriks, uus_maatriks)