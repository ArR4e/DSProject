# Trips-traps-trull

#Funktsioon sümbolite seisu kontrollimiseks
def kontrolli(sümbol, maatriks):
    sümboli_esinemine = 0
    
    #Horisontaane kontroll
    for i in range(len(maatriks)):
        for j in range(len(maatriks)-2):
            if maatriks[i][j] == sümbol and maatriks[i][j+1] == sümbol and maatriks[i][j+2] == sümbol:
                sümboli_esinemine += 1
    
    #Vertikaalne kontroll
    for i in range(len(maatriks)-2):
        for j in range(len(maatriks)):
            if maatriks[i][j] == sümbol and maatriks[i+1][j] == sümbol and maatriks[i+2][j] == sümbol:
                sümboli_esinemine += 1

    #Diagonaalne kontroll
    for i in range(len(maatriks)-2):
        for j in range(len(maatriks)-2):
            if maatriks[i][j] == sümbol and maatriks[i+1][j+1] == sümbol and maatriks[i+2][j+2] == sümbol:
                sümboli_esinemine += 1
    
    #Teistpidi diagonaali kontroll
    for i in range(len(maatriks)-2):
        for j in range(1, len(maatriks)-1):
            if maatriks[i][-j] == sümbol and maatriks[i+1][-1-j] == sümbol and maatriks[i+2][-2-j] == sümbol:
                sümboli_esinemine += 1

    return sümboli_esinemine

#Funktsioon laua seisu väljastamiseks
def võitja(maatriks):
    seis = {"O":0, "X":0}
    seis["O"] = kontrolli("O", maatriks)
    seis["X"] = kontrolli("X", maatriks)
    return seis



a = [[' ',' ',' ',' '],
     [' ',' ',' ',' '],
     [' ',' ',' ',' '],
     [' ',' ',' ',' ']]

print(võitja(a))