maatriks=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def transponeeriK(maatriks):
    uus=[[0 for col in range(len(maatriks))] for row in range(len(maatriks[0]))]
    
    for i in range(len(maatriks)-1,-1,-1):
        for j in range(len(maatriks[i])-1,-1,-1):
            uus[j][i]=maatriks[len(maatriks)-1-i][len(maatriks[0])-j-1]     
    
    return uus

transponeeriK(maatriks)

