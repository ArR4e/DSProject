def võitja(m):
    d = {"O":0,"X":0}
    test = ""
    for rida in range(len(m)):
        for i in range(len(m[rida])):
            for el in ("O","X"):
                if m[rida][i] == el:
                    if i < 2 and m[rida][i+1]==el and m[rida][i+2]==el: d[el] += 1
                    if rida < 2 and m[rida+1][i]==el and m[rida+2][i]==el: d[el] += 1
                    if i < 2 and rida < 2 and m[rida+1][i+1]==el and m[rida+2][i+2]==el: d[el] += 1
                    if i > 1 and rida < 2 and m[rida+1][i-1]==el and m[rida+2][i-2]==el: d[el] += 1
    return d
