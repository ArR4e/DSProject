sümbol = ''
def võitja(maatriks):
    global sümbol
    X_loendur = 0
    if sümbol == 'X':
        X_loendur += 1
    O_loendur = 0
    if sümbol == 'O':
        O_loendur += 1
    maatriks = [[1,2,3,4],[5,6,7,8]]
    for i in range(2):
        for j in range(2):
            print(maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2])
    maatriks = [[1,2], [3,4],[5,6],[7,8]]
    for i in range(2):
        for j in range(2):
            print(maatriks[i][j]+maatriks[i+1][j]+maatriks[i+2][j])
    maatriks = [[1,2,3],[4,5,6],[7,8,9]]
    for i in range(2):
        for j in range(2):
            print(maatriks[i][j]+maatriks[i+1][j+1])
    maatriks = [[1,2,3],[4,5,6],[7,8,9]]
    for i in range(2):
        for j in range(2):
            print(maatriks[i][j+1]+maatriks[i+1][j])
    sõnastik1 = {}
    sõnastik1["võti"] = 1
    sõnastik2 = {"võti1":1,"võti2":2}
    return maatriks
print(võitja([1,2,3,4]))