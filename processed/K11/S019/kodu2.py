def transponeeriK(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j], m[len(m)-j][len(m[i])-i] = m[len(m)-i][len(m[i])-j], m[i][j]