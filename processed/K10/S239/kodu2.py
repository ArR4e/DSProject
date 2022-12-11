def horisontaalne(maatriks,sümbol):
    loendur=0
    for i in range(2):
        for j in range(2):
            if maatriks[i][j]==sümbol:
                if maatriks[i][j+1]==sümbol:
                    if maatriks[i][j+2]==sümbol:
                        loendur+=1
    return loendur

def vertikaalne(maatriks,sümbol):
    loendur=0
    for i in range(2):
        for j in range(2):
            if maatriks[i][j]==sümbol:
                if maatriks[i+1][j]==sümbol:
                    if maatriks[i+2][j]==sümbol:
                        loendur+=1
    return loendur

def diagonaalne(maatriks,sümbol):
    loendur=0
    for i in range(2):
        for j in range(2):
            if maatriks[i][j]==sümbol:
                if maatriks[i+1][j+1]==sümbol:
                    if maatriks[i+2][j+2]==sümbol:
                        loendur+=1
    for i in range(2,4):
        for j in range(2):
            if maatriks[i][j]==sümbol:
                if maatriks[i-1][j+1]:
                    if maatriks[i-2][j+2]:
                        loendur+=1
    return loendur

def võitja(maatriks):
    seis={"O":{},"X":{}}
    seis["O"]=horisontaalne(maatriks,"O")+vertikaalne(maatriks,"O")+diagonaalne(maatriks,"O")
    seis["X"]=horisontaalne(maatriks,"X")+vertikaalne(maatriks,"X")+diagonaalne(maatriks,"X")
    return seis