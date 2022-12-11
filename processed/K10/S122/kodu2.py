def veerg(maatriks,tähis):
    kogus = 0
    for i in range(len(maatriks)-2):
        for j in range (len(maatriks[0])):
            if maatriks[i][j] == tähis and maatriks[i+1][j] == tähis and maatriks[i+2][j] == tähis:
                kogus+=1
    return(kogus)
                   
def rida(maatriks,tähis):   
    kogus=0
    for i in range(len(maatriks)):
        for j in range (len(maatriks[0])-2):
            if maatriks[i][j] == tähis and maatriks[i][j+1] == tähis and maatriks[i][j+2] == tähis:
                kogus+=1
    return(kogus)

def diagonaal_paremale(maatriks,tähis):   
    kogus=0
    for i in range(len(maatriks)-2):
        for j in range (len(maatriks[0])-2):
            if maatriks[i][j] == tähis and maatriks[i+1][j+1] == tähis and maatriks[i+2][j+2] == tähis:
                kogus+=1
    return(kogus)
    
def diagonaal_vasakule(maatriks,tähis):
    kogus = 0
    for i in range(len(maatriks)-2):
        for j in range (2,len(maatriks[0])):
            if maatriks[i][j] == tähis and maatriks[i+1][j-1] == tähis and maatriks[i+2][j-2] == tähis:
                kogus+=1
    return(kogus)

def võitja(maatriks):
    kogused = {}
    kogused["O"]=rida(maatriks,"O")+veerg(maatriks,"O")+diagonaal_paremale(maatriks,"O")+diagonaal_vasakule(maatriks,"O")
    kogused["X"]=rida(maatriks,"X")+veerg(maatriks,"X")+diagonaal_paremale(maatriks,"X")+diagonaal_vasakule(maatriks,"X")
    return kogused