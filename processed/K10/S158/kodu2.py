maatriks = [[" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "]]
X_arv = 0
O_arv = 0
def võitja(maatriks) :
    if sümbol == "X":
        X_arv += 1
    elif sümbol == "O":
        O_arv += 1
        
    i = 0
    j = 0
    #rea kontroll
    for i in range(4):
        if maatriks[i][0]==maatriks[i][1]==maatriks[i][2]==maatriks[i][3]==sümbol:
            #print()
            break
        i += 1
    #kolonni kontroll
    for j in range(4):
        if maatriks[0][j]==maatriks[1][j]==maatriks[2][j]==maatriks[3][j]==sümbol:
            #print()
            break
        j += 1
    #peadiagonaali kontroll
    if maatriks[0][0]==maatriks[1][1]==maatriks[2][2]==maatriks[3][3]==sümbol:
        #print()
    elif maatriks[0][3]==maatriks[1][2]==maatriks[2][1]==maatriks[3][0]==sümbol:
        #print()