def võitja(maatriks):
    arv_o = 0
    arv_x = 0
    for i in range(len(maatriks)):
        for j in range(len(maatriks[i])):
            if "X" == maatriks[i][j]:
                if j <= 1:
                    if "X" == maatriks[i][j+1] and "X" == maatriks[i][j+2]:
                        arv_x += 1           
                if i <= 1:
                    if "X" == maatriks[i+1][j] and "X" == maatriks[i+2][j]:
                        arv_x += 1        
                if j <= 1 and i <= 1:
                    if "X" == maatriks[i+1][j+1] and "X" == maatriks[i+2][j+2]:
                        arv_x += 1
                if j >= 2 and i <= 1:
                    if "X" == maatriks[i+1][j-1] and "X" == maatriks[i+2][j-2]:
                        arv_x += 1
            if "O" == maatriks[i][j]:
                if j <= 1:
                    if "O" == maatriks[i][j+1] and "O" == maatriks[i][j+2]:
                        arv_o += 1
                if i <= 1:
                    if "O" == maatriks[i+1][j] and "O" == maatriks[i+2][j]:
                        arv_o += 1
                if j <= 1 and i <= 1:
                    if "O" == maatriks[i+1][j+1] and "O" == maatriks[i+2][j+2]:
                        arv_o += 1
                if j >= 2 and i <= 1:
                    if "O" == maatriks[i+1][j-1] and "O" == maatriks[i+2][j-2]:
                        arv_o += 1
    d = {"O": arv_o, "X": arv_x}
    return d