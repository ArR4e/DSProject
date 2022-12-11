def võitja(matrix):
    x = 0
    o = 0
    d = {}
    for i in range(len(matrix)):
        if matrix[i].count('X') == 4:
            x += 2
        elif matrix[i].count('X') == 3:
            if ' ' in matrix[i]:
                if matrix[i].index(' ') == 0 or matrix[i].index(' ') == 3:
                    x += 1
            elif 'O' in matrix[i]:
                if matrix[i].index('O') == 0 or matrix[i].index('O') == 3:
                    x += 1
    zipped_rows = zip(*matrix)
    transposed_matrix = [list(row) for row in zipped_rows]
    for i in range(len(transposed_matrix)):
        if transposed_matrix[i].count('X') == 4:
            x += 2
        elif transposed_matrix[i].count('X') == 3:
            if ' ' in transposed_matrix[i]:
                if transposed_matrix[i].index(' ') == 0 or transposed_matrix[i].index(' ') == 3:
                    x += 1
            elif 'O' in transposed_matrix[i]:
                if transposed_matrix[i].index('O') == 0 or transposed_matrix[i].index('O') == 3:
                    x += 1
    if matrix[1][0] == matrix[2][1] == matrix[3][2] == 'X': 
        x += 1
    if matrix[2][0] == matrix[1][1] == matrix[0][2] == 'X':
        x += 1
    if matrix[3][1] == matrix[2][2] == matrix[1][3] == 'X':
        x += 1
    if transposed_matrix[1][0] == transposed_matrix[2][1] == transposed_matrix[3][2] == 'X': 
        x += 1
    if matrix[0][0] == matrix[1][1] == matrix[2][2]  == 'X' or matrix[3][3] == matrix[1][1] == matrix[2][2]  == 'X':
        if matrix[0][0] == matrix[1][1] == matrix[2][2] == matrix[3][3] == 'X':
            x += 2
        else:
            x += 1
    if matrix[0][3] == matrix[1][2] == matrix[2][1] == 'X' or matrix[3][0] == matrix[1][2] == matrix[2][1] == 'X':
        if matrix[3][0] == matrix[1][2] == matrix[2][1] == matrix[0][3] == 'X':
            x += 2
        else:
            x += 1
        
    
     ###   
        
    for i in range(len(matrix)):
        if matrix[i].count('O') == 4:
            o += 2
        elif matrix[i].count('O') == 3:
            if ' ' in matrix[i]:
                if matrix[i].index(' ') == 0 or matrix[i].index(' ') == 3:
                    o += 1
            elif 'X' in matrix[i]:
                if matrix[i].index('X') == 0 or matrix[i].index('X') == 3:
                    o += 1

    for i in range(len(transposed_matrix)):
        if transposed_matrix[i].count('O') == 4:
            o += 2
        elif transposed_matrix[i].count('O') == 3:
            if ' ' in transposed_matrix[i]:
                if transposed_matrix[i].index(' ') == 0 or transposed_matrix[i].index(' ') == 3:
                    o += 1
            elif 'X' in matrix[i]:
                if transposed_matrix[i].index('X') == 0 or transposed_matrix[i].index('X') == 3:
                    o += 1
    if matrix[1][0] == matrix[2][1] == matrix[3][2] == 'O': 
        o += 1
    if matrix[2][0] == matrix[1][1] == matrix[0][2] == 'O':
        o += 1
    if matrix[3][1] == matrix[2][2] == matrix[1][3] == 'O':
        o += 1
    if transposed_matrix[1][0] == transposed_matrix[2][1] == transposed_matrix[3][2] == 'O': 
        o += 1
    if matrix[0][0] == matrix[1][1] == matrix[2][2]  == 'O' or matrix[3][3] == matrix[1][1] == matrix[2][2]  == 'O':
        if matrix[0][0] == matrix[1][1] == matrix[2][2] == matrix[3][3] == 'O':
            o += 2
        else:
            o += 1
    if matrix[0][3] == matrix[1][2] == matrix[2][1] == 'O' or matrix[3][0] == matrix[1][2] == matrix[2][1] == 'O':
        if matrix[3][0] == matrix[1][2] == matrix[2][1] == matrix[0][3] == 'O':
            o += 2
        else:
            o += 1
    
    
    d['O'] = o
    d['X'] = x
    return(d)
    
    


