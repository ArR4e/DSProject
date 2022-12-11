maatriks = [[' ', 'O', 'X', ' '],
            [' ', 'O', 'X', ' '],
            [' ', 'O', 'X', ' '],
            [' ', 'O', 'X', ' ']]
 

def võitja(maatriks):
    d = {}
    a = ('X', 'O')
    for valik in a:
        k=0
        sinine =[0, 2,1]
        for i in range(2):
            if i <1:
                for m in range(0,4):
                    if maatriks[i+m][i] == valik and maatriks[i+m][i+1] == valik and maatriks[i+m][i+2] == valik:
                        k +=1
                    if maatriks[i+m][i+1] == valik and maatriks[i+m][i+2] == valik and maatriks[i+m][i+3] == valik:
                            k+=1
            if i< 1:
                for j in range(4):
                    try:
                        if maatriks[i][i+j] == valik and maatriks[i+1][i+j] == valik and maatriks[i+2][i+j] == valik:
                            k+=1
                    except:
                        continue
            for j in range(4):
                try:
                    if maatriks[i+1][i+j] == valik and maatriks[i+2][i+j] == valik and maatriks[i+3][i+j] == valik:
                        k+=1
                except:
                    continue
            if i < 2:
                for j in range(0, 2):
                    if maatriks[i][i+j] == valik and maatriks[i+1][i+1+j] == valik and maatriks[i+2][i+2+j] == valik:
                        k+= 1
            for j in range(2, 4):
                    if maatriks[i][j] == valik and maatriks[i][j-1] == valik and maatriks[i][j-2] == valik:
                        k+=1
            d[valik] = k
                    
    return d
                
            
                 
print(võitja(maatriks))
     