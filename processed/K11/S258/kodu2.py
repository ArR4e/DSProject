def transponeeriK(mat):
    m=len(mat)
    n=len(mat[0])
    mat2=[]
    for y in range(n):
        rida=[]
        for x in range(m):
            rida.append(mat[m-x-1][n-y-1])
        mat2.append(rida)
    return mat2