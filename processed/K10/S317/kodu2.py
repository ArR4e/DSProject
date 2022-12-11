def võitja(a):
    võidudx = 0
    võidudy = 0
    for i in a:
        if i[0] == "X"  and i[1] == "X" and i[2] == "X":
            võidudx += 1
        if i[1] == "X"  and i[2] == "X" and i[3] == "X":
            võidudx += 1
        if i[0] == "O"  and i[1] == "O" and i[2] == "O":
            võidudy += 1
        if i[1] == "O"  and i[2] == "O" and i[3] == "O":
            võidudy += 1               
    järjend = []
    for i in a:
        for j in i:
            järjend.append(j)
    lisajärjend = [0, 4, 8, 12]
    lisajärjend2 = [3, 6]
    for i in lisajärjend:
        try:
            if järjend[i] == "X" and järjend[i+5] == "X" and järjend[i+10] == "X":
                võidudx += 1
            if järjend[i+1] == "X" and järjend[i+6] == "X" and järjend[i+11] == "X":
                võidudx += 1
#            if järjend[i-1] == "X" and järjend[i+4] == "X" and järjend[i+9] == "X":
#                võidudx += 1
            if järjend[i] == "O" and järjend[i+5] == "O" and järjend[i+10] == "O":
                võidudy += 1
            if järjend[i+1] == "O" and järjend[i+6] == "O" and järjend[i+11] == "O":
                võidudy += 1
#            if järjend[i-1] == "O" and järjend[i+4] == "O" and järjend[i+9] == "O":
#                võidudy += 1
        except:
            continue
    for i in lisajärjend2:
        try:
            if järjend[i] == "X" and järjend[i+3] == "X" and järjend[i+6] == "X":
                võidudx += 1
            if järjend[i+4] == "X" and järjend[i+7] == "X" and järjend[i+10] == "X":
                võidudx += 1
            if järjend[2] == "X" and järjend[5] == "X" and järjend[8] == "X":
                võidudx += 1
            if järjend[i] == "O" and järjend[i+3] == "O" and järjend[i+6] == "O":
                võidudy += 1
            if järjend[i+4] == "O" and järjend[i+7] == "O" and järjend[i+10] == "O":
                võidudy += 1
        except:
            continue
        if järjend[2] == "O" and järjend[5] == "O" and järjend[8] == "O":
                võidudy += 1
    for i in range(0, len(järjend)):
        try:
            if järjend[i] == "X" and järjend[i+4] == "X" and järjend[i+8]== "X":
                võidudx += 1
            if järjend[i] == "O" and järjend[i+4] == "O" and järjend[i+8]== "O":
                võidudy += 1
        except:
            continue
    sõnastik = dict()
    sõnastik["O"] = võidudy
    sõnastik["X"] = võidudx
    return sõnastik