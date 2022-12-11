def programm(file):
    f = open(file, "r")
    bussid = [line.split() for line in f]
    f.close()
    for i in range(len(bussid)):
        max = i
        for j in range(i+1, len(bussid)):
            if bussid[j][2] < bussid[max][2] and bussid[j][0] < bussid[max][0] and bussid[j][1] > bussid[max][1]:
                max = j
        if i != max:
            bussid[i], bussid[max] = bussid[max], bussid[i]
    return bussid
print(programm("sõiduplaan.txt"))