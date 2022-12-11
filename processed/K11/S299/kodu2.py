def transponeeriK(m):
    järjend=[]
    for i in range(len(m[0])-1,-1,-1):
        uus=[]
        for j in range(len(m)-1,-1,-1):
            uus= uus + [m[j][i]]
        järjend.append(uus)
    return järjend

transponeeriK([[1, 2, 3], [4, 5, 6], [7, 8, 9]])