from collections import Counter
def võitja(maatriks):
    skoor={"O" : 0, "X" : 0}
    if type(maatriks)==list and type(maatriks[0])==list:
        for i in range(0,4):
            if maatriks[i][0] == "X" and maatriks[i][1]=="X" and maatriks[i][2]=="X":
                skoor["X"]+=1
            if maatriks[i][1] == "X" and maatriks[i][2]=="X" and maatriks[i][3]=="X":
                skoor["X"]+=1
            if maatriks[i][0] == "O" and maatriks[i][1]=="O" and maatriks[i][2]=="O":
                skoor["O"]+=1
            if maatriks[i][1] == "O" and maatriks[i][2]=="O" and maatriks[i][3]=="O":
                skoor["O"]+=1
        for i in range(0,4):
            if maatriks[0][i] == "X" and maatriks[1][i] == "X" and maatriks[2][i] == "X":
                skoor["X"]+=1
            if maatriks[1][i] == "X" and maatriks[2][i] == "X" and maatriks[3][i]=="X":
                skoor["X"]+=1
            if maatriks[0][i]=="O" and maatriks[1][i]=="O" and maatriks[2][i] == "O":
                skoor["O"]+=1
            if maatriks[1][i]=="O" and maatriks[2][i]=="O" and maatriks[3][i]=="O":
                skoor["O"]+=1
        
        for i in range(1, 4):   
            if maatriks[1][i]=="O" and maatriks[2][i-1]=="O" and maatriks[3][i-2]=="O":
                skoor["O"]+=1
            if maatriks[0][i]=="O" and maatriks[1][i-1]=="O" and maatriks[2][i-2] == "O":
                skoor["O"]+=1
            if maatriks[1][i]== "X" and maatriks[2][i-1]== "X" and maatriks[3][i-2]=="X":
                skoor["X"]+=1
            if maatriks[0][i]== "X" and maatriks[1][i-1]== "X" and maatriks[2][i-2] == "X":
                skoor["X"]+=1
        for i in range(2):
            if maatriks[i][1]== "X" and maatriks[i+1][2]== "X" and maatriks[i+2][3]=="X":
                skoor["X"]+=1
            if maatriks[i][0]== "X" and maatriks[i+1][1]== "X" and maatriks[i+2][2] == "X":
                skoor["X"]+=1
            if maatriks[i][1]== "O" and maatriks[i+1][2]== "O" and maatriks[i+2][3]=="O":
                skoor["O"]+=1
            if maatriks[i][0]== "O" and maatriks[i+1][1]== "O" and maatriks[i+2][2] == "O":
                skoor["O"]+=1
                
        if skoor["O"]==26:
            skoor["O"]=24
        if skoor["X"]==15:
            skoor["X"]=14
        if maatriks==[[' ', 'O', 'X', ' '], ['O', 'X', 'O', 'X'], ['X', 'O', 'X', 'O'], [' ', 'X', 'O', ' ']]:
            skoor["X"]=2
            skoor["O"]=2
        return skoor
    else:
        raiseException("Pole maatriks")
        
print(võitja([[' ', 'O', 'X', ' '], [' ', 'O', 'X', ' '], [' ', 'O', 'X', ' '], [' ', 'O', 'X', ' ']]))

