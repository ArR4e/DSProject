def transponeeriK(array):
    k = [[] for i in range(len(array[0]))]
    for i in range(len(array[0])):
        for j in range(len(array)):
            k[i].append(array[len(array)-1-j][len(array[0])-1-i])
    return k