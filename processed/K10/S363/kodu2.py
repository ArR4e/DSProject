def võitja(maatriks):
    def kokku(m, n):
        kokku = 0
        for i in range(len(m)):
            for j in range(len(m[i])):
                try:
                    if m[i][j] == n:
                        if m[i+1][j] == n:
                            if m[i+2][j] == n:
                                kokku += 1
                              
                except:
                    continue
 
        for i in range(len(m)):
            for j in range(len(m[i])):
                try:
                    if m[i][j] == n:
                        if m[i][j+1] == n:
                            if m[i][j+2] == n:
                                kokku += 1                                    

                except:
                    continue

        for i in range(len(m)):
            for j in range(len(m[i])):
                try:
                    if m[i][j] == n:
                        if m[i+1][j+1] == n:
                            if m[i+2][j+2] == n:
                                kokku += 1
                                                                    
                except:
                    continue
                
        for i in range(len(m)):
            for j in range(len(m[i])):
                try:
                    if m[i][j] == n:
                        if m[i+1][j-1] == n and j-1 >= 0:
                            if m[i+2][j-2] == n and j-2 >= 0:
                                kokku += 1
                               
                except:
                    continue
                
        return kokku
    
    d = {}
    d["O"] = kokku(maatriks, "O")
    d["X"] = kokku(maatriks, "X")
    
    return d
