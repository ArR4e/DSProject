def võitja(maatriks):
    d={"O":0,"X":0}
    for rida in maatriks:
        if rida[0]==rida[1]==rida[2]==rida[3]=="X" or rida[0]==rida[1]==rida[2]=="X" or rida[1]==rida[2]==rida[3]=="X":
            d["X"]=d["X"]+1
        elif rida[0]==rida[1]==rida[2]==rida[3]=="O" or rida[0]==rida[1]==rida[2]=="O" or rida[1]==rida[2]==rida[3]=="O":
            d["O"]=d["O"]+1
    for number in range(0,4):
        if maatriks[0][number]==maatriks[1][number]==maatriks[2][number]==maatriks[3][number]=="X" or maatriks[0][number]==maatriks[1][number]==maatriks[2][number]=="X" or maatriks[1][number]==maatriks[2][number]==maatriks[3][number]=="X":
            d["X"]=d["X"]+1
        elif maatriks[0][number]==maatriks[1][number]==maatriks[2][number]==maatriks[3][number]=="O" or maatriks[0][number]==maatriks[1][number]==maatriks[2][number]=="O" or maatriks[1][number]==maatriks[2][number]==maatriks[3][number]=="O":
            d["O"]=d["O"]+1
    if maatriks[0][0]==maatriks[1][1]==maatriks[2][2]==maatriks[3][3]=="X" or maatriks[0][0]==maatriks[1][1]==maatriks[2][2]=="X" or maatriks[1][1]==maatriks[2][2]==maatriks[3][3]=="X" or maatriks[0][3]==maatriks[1][2]==maatriks[2][1]==maatriks[3][0]=="X" or maatriks[0][3]==maatriks[1][2]==maatriks[2][1]=="X" or maatriks[1][2]==maatriks[2][1]==maatriks[3][0]=="X":
        d["X"]=d["X"]+1
    elif maatriks[0][0]==maatriks[1][1]==maatriks[2][2]==maatriks[3][3]=="O" or maatriks[0][0]==maatriks[1][1]==maatriks[2][2]=="O" or maatriks[1][1]==maatriks[2][2]==maatriks[3][3]=="O" or maatriks[0][3]==maatriks[1][2]==maatriks[2][1]==maatriks[3][0]=="O" or maatriks[0][3]==maatriks[1][2]==maatriks[2][1]=="O" or maatriks[1][2]==maatriks[2][1]==maatriks[3][0]=="O":
        d["O"]=d["O"]+1
    return d

print(võitja([['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']]))