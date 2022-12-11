def transponeeriK(mat):
    uus_mat = []
    for i in range((len(mat[0])-1), -1, -1):
        uus = []
        uus_mat.append(uus)
        for j in range((len(mat)-1), -1, -1):
            uus.append((mat[j][i]))
    return uus_mat