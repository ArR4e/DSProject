def transponeeriK(sisend):
    tagastus = []
    x = len(sisend[0]) -1
    y = 0
    for i in range(len(sisend[0])):
        tagastus.append([])
    for i in range(len(sisend[0])):
        for j in range(len(sisend)):
            if y == len(sisend):
                x = x-1
                y = 0
            tagastus[i].append(sisend[len(sisend)-y-1][x])
            y += 1
    return(tagastus)
    
    
print(transponeeriK([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]))
print(transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(transponeeriK([[4, 31, 67, 99]]))