#mirjampirn

def test_rida(seis, symbol, x, y):
    return 1 if seis[y][x]==symbol and seis[y][x+1]==symbol and seis[y][x+2]==symbol else 0

def test_veerg(seis, symbol, x, y):
    return 1 if seis[y][x]==symbol and seis[y+1][x]==symbol and seis[y+2][x]==symbol else 0

def test_diagonaal(seis, symbol, x, y, langev=True):
    if langev:
        return 1 if seis[y][x]==symbol and seis[y+1][x+1]==symbol and seis[y+2][x+2]==symbol else 0
    else:
        return 1 if seis[y][x]==symbol and seis[y+1][x-1]==symbol and seis[y+2][x-2]==symbol else 0

def test_read(seis, symbol):
    n=0
    for y in range(4):
        n += test_rida(seis,symbol, 0, y)
        n += test_rida(seis, symbol, 1, y)
    return n

def test_veerud(seis, symbol):
    n=0
    for x in range(4):
        n += test_veerg(seis, symbol, x, 0)
        n += test_veerg(seis, symbol, x, 1)
    return n

def test_diagonaalid(seis, symbol):
    n=0
    n += test_diagonaal(seis, symbol, 0, 0)
    n += test_diagonaal(seis, symbol, 1, 1)
    n += test_diagonaal(seis, symbol, 1, 0)
    n += test_diagonaal(seis, symbol, 0, 1)
    n += test_diagonaal(seis, symbol, 3, 0, langev= False)
    n += test_diagonaal(seis, symbol, 2, 1, langev= False)
    n += test_diagonaal(seis, symbol, 2, 0, langev= False)
    n += test_diagonaal(seis, symbol, 3, 1, langev= False)
    return n

def võitja(seis):
    kolmesed={"O":0, "X":0}
    kolmesed["O"] += test_read(seis, "O")
    kolmesed["O"] +=test_veerud(seis, "O")
    kolmesed["O"] +=test_diagonaalid(seis, "O")
    kolmesed["X"] +=test_read(seis, "X")
    kolmesed["X"] +=test_veerud(seis, "X")
    kolmesed["X"] +=test_diagonaalid(seis, "X")
    return kolmesed