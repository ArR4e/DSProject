def loenda(m, symbol):
    rida = symbol * 3
    read = 0
    
    # Diagonaalid
    for i in range(2):
        if m[0][1] + m[1][2] + m[2][3] == rida:
            read += 1
            
        if m[0][0] + m[1][1] + m[2][2] == rida:
            read += 1
            
        if m[1][1] + m[2][2] + m[3][3] == rida:
            read += 1
            
        if m[1][0] + m[2][1] + m[3][2] == rida:
            read += 1
        m.reverse()
        
    # Horisontaal ja vertikaal
    for j in range(2):
        if j:
            _m = list(list(x) for x in zip(*m))[::-1]
        else:
            _m = m[:]
        
        for veerg in _m:
            if veerg[0] + veerg[1] + veerg[2] == rida:
                read += 1
            
            if veerg[1] + veerg[2] + veerg[3] == rida:
                read += 1
            
    return read

def võitja(maatriks):
    return {"O": loenda(maatriks, "O"), "X": loenda(maatriks, "X")}
