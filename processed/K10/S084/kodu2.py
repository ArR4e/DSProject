def võitja(seis):
    tulemus = {"O":0,"X":0}
    for i in range(len(seis)):
        for j in range(len(seis[0])):
            if 0 < j < len(seis[0])-1 and seis[i][j-1] == seis[i][j] == seis[i][j+1] != " ":
                tulemus[seis[i][j]] += 1
            if 0 < i < len(seis)-1 and seis[i-1][j] == seis[i][j] == seis[i+1][j] != " ":
                tulemus[seis[i][j]] += 1
            if 0 < i < len(seis)-1 and 0 < j < len(seis[0])-1 and seis[i-1][j-1] == seis[i][j] == seis[i+1][j+1] != " ":
                tulemus[seis[i][j]] += 1
            if 0 < i < len(seis)-1 and 0 < j < len(seis[0])-1 and seis[i-1][j+1] == seis[i][j] == seis[i+1][j-1] != " ":
                tulemus[seis[i][j]] += 1
    return tulemus