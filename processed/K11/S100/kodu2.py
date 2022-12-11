def transponeeriK(arr):
    
    out = [[0]*len(arr) for i in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            out[-(j+1)][-(i+1)] = arr[i][j]

    return out
