def diagonaal(x,maatriks):
    kokku = 0
    i = 0
    j = 0
    if (maatriks[i][j] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == x): # ülevalt alla 1 
        kokku += 1
    if (maatriks[i+3][j+3] == maatriks[i+1][j+1] == maatriks[i+2][j+2] == x): #alt üles 1 
        kokku += 1
    if (maatriks[i][j+3] == maatriks[i+1][j+2] == maatriks[i+2][j+1] == x): # ülevalt alla 2
        kokku += 1
    if (maatriks[i+1][j+2] == maatriks[i+2][j+1] == maatriks[i+3][j+0] == x):
        kokku += 1
    
    return kokku

def horisontaal(x,maatriks):
    kokku = 0
    j = 0
    i = 0
    while i < 4:
        if (maatriks[i][j] == maatriks[i][j+1] == maatriks[i][j+2] == x):
            kokku += 1
        if (maatriks[i][j+1] == maatriks[i][j+2] == maatriks[i][j+3] == x):
            kokku += 1
        i += 1
    
    return kokku

def vertikaal(x,maatriks):
    j = 0
    i = 0
    kokku = 0
    while j < 4:
        if (maatriks[i][j] == maatriks[i+1][j] == maatriks[i+2][j] == x):
            kokku += 1
        if (maatriks[i+1][j] == maatriks[i+2][j] == maatriks[i+3][j] == x):
            kokku += 1
        
        j+= 1
    
    return kokku
    

def võitja(maatriks):
    sõnastik = {}
    x_kokku = diagonaal('X',maatriks) + vertikaal('X',maatriks) + horisontaal('X',maatriks)+diagonaalid_2('X',maatriks)
    nullid = diagonaal('O',maatriks) + vertikaal('O',maatriks) + horisontaal('O',maatriks)+diagonaalid_2('O',maatriks)
    sõnastik['O'] = nullid
    sõnastik['X'] = x_kokku
    
    return sõnastik
    
    
def diagonaalid_2(x,maatriks):
    j = 0
    i = 0
    kokku = 0
    if (maatriks[i][j+2] == maatriks[i+1][j+1] == maatriks[i+2][j] == x):
        kokku += 1
    if (maatriks[i+3][j+1] == maatriks[i+2][j+2] == maatriks[i+1][j+3] == x):
        kokku += 1
    if (maatriks[i][j+1] == maatriks[i+1][j+2] == maatriks[i+2][j+3] == x):
        kokku += 1
    if (maatriks[i+1][j] == maatriks[i+2][j+1] == maatriks[i+3][j+2] == x):
        kokku += 1
    
    return kokku
    