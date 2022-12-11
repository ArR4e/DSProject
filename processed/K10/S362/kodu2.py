def võitja(listide_list):
    for i in range(len(listide_list)):
        for j in range(len(listide_list)):
            listide_list[i][j]=listide_list[i][j].upper()
            
    
    sõnastik={}
    lugeja1=0
    lugeja2=0
    for i in range(len(listide_list)):# loeb ridade kaupa
        j=0
        if listide_list[i][j]==listide_list[i][j+1]==listide_list[i][j+2]!=" " and listide_list[i][j+1]==listide_list[i][j+2]==listide_list[i][j+3]!=" ":
            if listide_list[i][j+1]=="X":
                lugeja1=lugeja1+2
            else:
                lugeja2=lugeja2+2
        
        elif listide_list[i][j]==listide_list[i][j+1]==listide_list[i][j+2]!=" " or listide_list[i][j+1]==listide_list[i][j+2]==listide_list[i][j+3]!=" ":
            if listide_list[i][j+1]=="X":
                lugeja1=lugeja1+1
            else:
                lugeja2=lugeja2+1
    for j in range(len(listide_list)): # loeb "tulpade" kaupa
        i=0
        
        if listide_list[i][j]==listide_list[i+1][j]==listide_list[i+2][j]!=" " and listide_list[i+1][j]==listide_list[i+2][j]==listide_list[i+3][j]!=" " :
            if listide_list[i+1][j]=="X":
                lugeja1=lugeja1+2
            else:
                lugeja2=lugeja2+2
        elif listide_list[i][j]==listide_list[i+1][j]==listide_list[i+2][j]!=" " or listide_list[i+1][j]==listide_list[i+2][j]==listide_list[i+3][j]!=" " :
            if listide_list[i+1][j]=="X":
                lugeja1=lugeja1+1
            else:
                lugeja2=lugeja2+1 
   
    i=0
    j=0
    if listide_list[i][j]==listide_list[i+1][j+1]==listide_list[i+2][j+2]!=" " :
        if listide_list[i+1][j+1]=="X":
            lugeja1=lugeja1+1
        else:
            lugeja2=lugeja2+1
    if listide_list[i+1][j+1]==listide_list[i+2][j+2]==listide_list[i+3][j+3]!=" ":
        if listide_list[i+1][j+1]=="X":
            lugeja1=lugeja1+1
        else:
            lugeja2=lugeja2+1
    if listide_list[i][j+3]==listide_list[i+1][j+2]==listide_list[i+2][j+1]!=" " :
        if listide_list[i+1][j+2]=="X":
            lugeja1=lugeja1+1
        else:
            lugeja2=lugeja2+1   
    if listide_list[i+1][j+2]==listide_list[i+2][j+1]==listide_list[i+3][j]!=" ":
        if listide_list[i+1][j+2]=="X":
            lugeja1=lugeja1+1
        else:
            lugeja2=lugeja2+1
    if listide_list[i][j+2]==listide_list[i+1][j+1]==listide_list[i+2][j]!=" ":
        if listide_list[i+1][j+1]=="X":
            lugeja1=lugeja1+1
        else:
            lugeja2=lugeja2+1
    if listide_list[i+1][j]==listide_list[i+2][j+1]==listide_list[i+3][j+2]!=" ":
        if listide_list[i+2][j+1]=="X":
            lugeja1=lugeja1+1
        else:
            lugeja2=lugeja2+1
    if listide_list[i][j+1]==listide_list[i+1][j+2]==listide_list[i+2][j+3]!=" ":
        if listide_list[i+1][j+2]=="X":
            lugeja1=lugeja1+1
        else:
            lugeja2=lugeja2+1
    if listide_list[i+1][j+3]==listide_list[i+2][j+2]==listide_list[i+3][j+1]!=" ":
        if listide_list[i+2][j+2]=="X":
            lugeja1=lugeja1+1
        else:
            lugeja2=lugeja2+1
    for i in range(2):
        Liikmed=['O', 'X']
        lugejad=[lugeja2, lugeja1]
        sõnastik[Liikmed[i]]=lugejad[i]
#     print(lugeja1,"x") # X-d
#     print(lugeja2, "O") # O-d
    # print(sõnastik)
    return sõnastik
    
    
# listide_list=[['O',' ',' ','X'],
#             [' ','O','X',' '],
#             [' ','X','O',' '],
#             ['X',' ',' ','O']]


# listide_list=[[' ',' ',' ',' '],
#             [' ',' ',' ',' '],
#             [' ',' ',' ',' '],
#             [' ',' ',' ',' ']]
# listide_list=[['O',' ','O','X'],
#             ['O','O','X','X'],
#             ['O','X','O',' '],
#             ['X','X','X','O']]
# listide_list=[['X','X','X',' '],
#             [' ','O',' ',' '],
#             [' ',' ','O',' '],
#             [' ',' ',' ','O']]



# [['X','X','X',' '],
#             [' ','O',' ',' '],
#             [' ',' ','O',' '],
#             [' ',' ',' ','O']]

#Mittetöödanud versioonid:

# Need tulemused andsid vigase tulemuse:
# 1)
# listide_list=[[' ', 'X', ' ', 'O'],
#               [' ', 'X', ' ', 'O'],
#               [' ', 'X', ' ', 'O'],
#               [' ', ' ', ' ', ' ']] #pidi andma {'O': 1, 'X': 1}, aga andis {'O': 2, 'X': 0}

# 2)
# listide_list=[[' ', 'O', 'X', ' '],
#               [' ', 'O', 'X', ' '],
#               [' ', 'O', 'X', ' '],
#               [' ', 'O', 'X', ' ']] #pidi andma {'O': 2, 'X': 2}, aga andis {'O': 1, 'X': 1}
# 3)
listide_list=[['O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O']] # pidi andma {'O': 24, 'X': 0}, aga abdis {'O': 16, 'X': 0}.

print(võitja(listide_list))
