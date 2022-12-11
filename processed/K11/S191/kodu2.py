näidis=[[0,2,3],
        [3,4,3],
        [0,6,3]]

def transponeeriK(matrix):
    x_mõõt=len(matrix[0])
    y_mõõt=len(matrix)
    for y in range(y_mõõt):
        for x in range(x_mõõt):
            print(matrix[y][x])
    uus_matrix=[]
    for y in range(x_mõõt):
        uus_matrix+=[list(y_mõõt*(0,))]
    for y in range(y_mõõt):
        for x in range(x_mõõt):
            uus_matrix[x][y]=matrix[y_mõõt-y-1][x_mõõt-x-1]
    return(uus_matrix)
print(transponeeriK(näidis))