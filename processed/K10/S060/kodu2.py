def võitja(m):
    x=0
    y=0
    vastus={}
    for i in range(4):
        for j in range(2):
                if m[i][j]==m[i][j+1]==m[i][j+2]=="X":
                    x=x+1
                elif m[i][j]==m[i][j+1]==m[i][j+2]=="O":
                    y=y+1
    for i in range(2):
        for j in range(4):
            if m[i][j]==m[i+1][j]==m[i+2][j]=="X":
                x=x+1
            elif m[i][j]==m[i+1][j]==m[i+2][j]=="O":
                y=y+1
        for j in range(2):
            if m[i][j]==m[i+1][j+1]==m[i+2][j+2]=="X":
                x=x+1
            elif m[i][j]==m[i+1][j+2]==m[i+2][j+2]=="O":
                y=y+1
        for j in range(2,4):
            if m[i][j]==m[i+1][j-1]==m[i+2][j-2]=="X":
                x=x+1
            elif m[i][j]==m[i+1][j-2]==m[i+2][j-2]=="O":
                y=y+1
    vastus["O"]=y
    vastus["X"]=x
    return vastus


print(võitja([['O',' ','O','X'],

            ['O','O','X','X'],

            ['O','X','X',' '],

            ['X','X','X','O']]))
              
              