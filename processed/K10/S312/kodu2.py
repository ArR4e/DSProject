def võitja(matrix):
    o = symbol_korda('O', matrix)
    x = symbol_korda('X', matrix)
    sõnastik = {'O': 0, 'X': 0}
    sõnastik['O'] = o
    sõnastik['X'] = x         
    return sõnastik
    
def symbol_korda(s, matrix):
    s_kolmik = s * 3
    s_korda = 0                   
    #horisonbtaalne
    for i in range(4):
        for j in range(2):
            kolmik = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2]
            if kolmik == s_kolmik:
                s_korda += 1
    #verikaalne
    for i in range(2):
        for j in range(4):
            kolmik = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j]
            if kolmik == s_kolmik:
                s_korda += 1             
    #diagonaalid vasak-parem
    for i in range(2):
        for j in range(2):
            kolmik = matrix[i][j]+ matrix[i+1][j+1] + matrix[i+2][j+2]
            if kolmik == s_kolmik:
                s_korda += 1
                
     #diagonaal parem-vasak
    for i in range(2):
        for j in range(2):
            kolmik = matrix[i][j+2]+ matrix[i+1][j+1] + matrix[i+2][j]
            if kolmik == s_kolmik:
                s_korda += 1
    return s_korda             
                
                