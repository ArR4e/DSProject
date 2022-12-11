def reas_3(XO):
    võite = 0
    try:
        for a in XO:
            XO2 = XO.copy()
            XO2.remove(a)
            for b in XO2:
                XO3 = XO.copy()
                XO3.remove(a)
                for c in XO3:
                    if a[0]+2 == b[0]+1 == c[0] and a[1] == b[1] == c[1]:
                        võite += 1
                    elif a[1]+2 == b[1]+1 == c[1] and a[0] == b[0] == c[0]:
                        võite += 1
                    elif a[0]+2 == b[0]+1 == c[0] and a[1]+2 == b[1]+1 == c[1] or a[0]+2 == b[0]+1 == c[0] and a[1]-2 == b[1]-1 == c[1]:
                        võite += 1
    except:
        return võite
    return võite

def võitja(matrix):
    list_x = [(x,y) for y in range(len(matrix)) for x in range(len(matrix)) if matrix[y][x] == "X"]
    list_o = [(x,y) for y in range(len(matrix)) for x in range(len(matrix)) if matrix[y][x] == "O"]
    return {"X":reas_3(list_x), "O":reas_3(list_o)}