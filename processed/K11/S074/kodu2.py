#Maatriksi transponeerimis funktsioon
def transponeeriK(maatriks):
    
    #Transponeeritud kujul loplik maatriks
    transponeeritud = []
    for rida in range(len(maatriks[0]) -1, -1, -1):
        
        #Osa transponeeritud maatriksist
        transponeeritav = []
        for veerg in range(len(maatriks) -1, -1, -1):
            transponeeritav.append(maatriks[veerg][rida])
            
        #Lisa transponeeritud listi    
        transponeeritud.append(transponeeritav)
        
    #Transponeeritud maatriksi tagastamine   
    return transponeeritud



#print(transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
#print(transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]]))
#print(transponeeriK([[4, 31, 67, 99]]))


            
#Kusisin moningast abi ulessande lahendamisel kursusekaaslaselt :)