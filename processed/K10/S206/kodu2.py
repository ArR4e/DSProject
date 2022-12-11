a = [['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']]
def reas(a):
    X = 0
    O = 0
    for rida in a:
        for i in range(2):
            if rida[i] == rida[i+1] == rida[i+2]:
                if rida[i] == "X":
                    X +=1
                elif rida[i] == "O":
                    O +=1
    return (X, O)

def veerus(a):
    X = 0
    O = 0
    for i in range(2):
        for j in range(len(a[i])):
            if a[i][j] == a[i+1][j] == a[i+2][j]:
                if a[i][j] == "X":
                    X+=1
                elif a[i][j] == "O":
                    O +=1
    return(X, O)

def diag(a):
    X = 0
    O = 0
    for i in range(2):
        for j in range(2):
            if a[i][j] == a[i+1][j+1] == a[i+2][j+2]:
                if a[i][j] == "X":
                    X +=1
                elif a[i][j] == "O":
                    O +=1
    for i in range(len(a)-2):
        for j in range(len(a)-2):
            if a[i][len(a)-1-j] == a[i+1][len(a)-2-j] == a[i+2][len(a)-3-j]:
                if a[i][len(a)-1-j] == "X":
                    X += 1
                elif a[i][len(a)-1-j] == "O":
                    O += 1
    return (X, O)

def võitja(a):
    rida = reas(a)
    veerg = veerus(a)
    diago = diag(a)
    X = rida[0] + veerg[0] + diago[0]
    O = rida[1] + veerg[1] + diago[1]
    return {"O": O, "X": X}

print(võitja(a))
        
