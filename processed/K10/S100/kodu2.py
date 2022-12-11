def võitja(arr):
    out = {}
    ovoit = 0
    xvoit = 0
    
    #Read
    for i in range(len(arr)):
        for j in range(len(arr)-2):
            if arr[i][j] == arr[i][j+1] == arr[i][j+2] and arr[i][j] != ' ':
                if arr[i][j] == 'O':
                    ovoit += 1
                elif arr[i][j] == 'X':
                    xvoit += 1
    
    #Veerud
    for i in range(len(arr)-2):
        for j in range(len(arr)):
            if arr[i][j] == arr[i+1][j] == arr[i+2][j] and arr[i][j] != ' ':
                if arr[i][j] == 'O':
                    ovoit += 1
                elif arr[i][j] == 'X':
                    xvoit += 1
    
    #Peadiagonaalsed
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            if arr[i][j] == arr[i+1][j+1] == arr[i+2][j+2] and arr[i][j] != ' ':
                if arr[i][j] == 'O':
                    ovoit += 1
                elif arr[i][j] == 'X':
                    xvoit += 1
    
    #Kõrvaldiagonaalsed
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            if arr[i+2][j] == arr[i+1][j+1] == arr[i][j+2] and arr[i+1][j+1] != ' ':
                if arr[i+1][j+1] == 'O':
                    ovoit += 1
                elif arr[i+1][j+1] == 'X':
                    xvoit += 1
    
    out["O"] = ovoit
    out["X"] = xvoit
    
    return out
