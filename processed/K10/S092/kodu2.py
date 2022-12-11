def horizontal_n(arg, ch):
    hor_n = 0
    for vert in range(0,4):
        for hor in range(0,2):
            if arg[vert][hor] == ch and arg[vert][hor+1] == ch and arg[vert][hor+2] == ch:
                hor_n += 1
                
    return hor_n


def vertical_n(arg, ch):
    vert_n = 0
    for hor in range(0,4):
        for vert in range(0,2):
            if arg[vert][hor] == ch and arg[vert+1][hor] == ch and arg[vert+2][hor] == ch:
                vert_n += 1
                
    return vert_n


def diagonal_n(arg,ch):
    dia_n = 0
    for hor in range(0,2):
        for vert in range(0,2):
            if arg[vert][hor] == ch and arg[vert+1][hor+1] == ch and arg[vert+2][hor+2] == ch:
                dia_n += 1
                
    for hor in range(2,4):
        for vert in range(0,2):
            if arg[vert][hor] == ch and arg[vert+1][hor-1] == ch and arg[vert+2][hor-2] == ch:
                dia_n += 1
    
    return dia_n


def võitja(arg):
    hor_O = horizontal_n(arg, "O")
    hor_X = horizontal_n(arg, "X")
    
    vert_O = vertical_n(arg, "O")
    vert_X = vertical_n(arg, "X")

    dia_O = diagonal_n(arg, "O")
    dia_X = diagonal_n(arg, "X")
    #for hor in in range(0,2):
    #for vert in range(1,4)
    
    sum_n = {}
    sum_n["O"] = hor_O + vert_O + dia_O
    sum_n["X"] = hor_X + vert_X + dia_X
        
    return sum_n
    #print(hor_O)
    #print(ver_X)
    #print(dia_X)

#print(võitja([['O',' ','O','X'],
#            ['O','O','X','X'],
#            ['O','X','O',' '],
#            ['X','X','X','O']]))